from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.conf import settings
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token
import requests
from django.core.files.base import ContentFile
import uuid

from .serializers import (
    UserSerializer,
    UserProfileUpdateSerializer,
    GoogleAuthSerializer,
    UsernameCheckSerializer
)
from .models import UserProfile

User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def google_oauth_callback(request):
    serializer = GoogleAuthSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {'error': 'Invalid request data', 'details': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    access_token = serializer.validated_data['access_token']

    try:
        client_id = settings.GOOGLE_OAUTH_CLIENT_ID

        if not client_id:
            return Response(
                {'error': 'Server configuration error: CLIENT_ID not set'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        id_info = id_token.verify_oauth2_token(access_token, google_requests.Request(), audience=client_id)

        # Verify issuer
        if 'accounts.google.com' not in id_info.get('iss', ''):
            return Response(
                {'error': 'Invalid token issuer'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Verify audience
        if id_info.get('aud') != client_id:
            return Response(
                {'error': 'Invalid token audience'},
                status=status.HTTP_400_BAD_REQUEST
            )

        email = id_info['email']
        first_name = id_info.get('given_name', '')
        last_name = id_info.get('family_name', '')
        google_avatar_url = id_info.get('picture', None)

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'first_name': first_name,
                'last_name': last_name,
            }
        )

        if not created:
            user.first_name = first_name
            user.last_name = last_name
            user.save()

        # Download and save Google avatar
        if google_avatar_url and not user.avatar:
            try:
                response = requests.get(google_avatar_url, timeout=5)
                if response.status_code == 200:
                    filename = f'google_{uuid.uuid4().hex[:8]}.jpg'
                    user.avatar.save(filename, ContentFile(response.content), save=True)
            except Exception:
                pass

        if not hasattr(user, 'profile'):
            UserProfile.objects.create(user=user)

        # Create UserProgress for new users with Level 1 unlocked
        from quiz.models import UserProgress, Level
        if created or not hasattr(user, 'progress'):
            try:
                first_level = Level.objects.filter(level_number=1).first()
                UserProgress.objects.get_or_create(
                    user=user,
                    defaults={
                        'current_level': first_level,
                        'total_xp': 0,
                    }
                )
            except Exception:
                pass

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user': UserSerializer(user, context={'request': request}).data,
            'is_new_user': created,
            'username_required': created or not user.username,
        }, status=status.HTTP_200_OK)

    except ValueError:
        return Response(
            {'error': 'Token verification failed'},
            status=status.HTTP_400_BAD_REQUEST
        )
    except Exception:
        return Response(
            {'error': 'Authentication error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user

    if request.method == 'GET':
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserProfileUpdateSerializer(
            user,
            data=request.data,
            partial=True,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user.refresh_from_db()
        return Response(UserSerializer(user, context={'request': request}).data)


@api_view(['POST'])
@permission_classes([AllowAny])
def check_username(request):
    serializer = UsernameCheckSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response({
        'available': True,
        'message': 'Username is available'
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_username(request):
    username = request.data.get('username')
    avatar_file = request.FILES.get('avatar')  # For uploaded files
    avatar_id = request.data.get('avatar_id')  # For predefined avatars

    if not username:
        return Response(
            {'error': 'Username is required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exclude(id=request.user.id).exists():
        return Response(
            {'error': 'Username already exists'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = request.user
    user.username = username

    # Handle avatar
    if avatar_file:
        # Save uploaded file
        import os
        from django.core.files.storage import default_storage

        filename = f'avatars/{user.id}_{avatar_file.name}'
        filepath = default_storage.save(filename, avatar_file)
        user.avatar = filepath
    elif avatar_id:
        # Copy predefined avatar to user's avatar
        import shutil
        from django.core.files.storage import default_storage
        from pathlib import Path

        predefined_path = Path(settings.BASE_DIR) / 'static_assets' / 'avatars' / 'predefined' / f'{avatar_id}.png'
        if predefined_path.exists():
            user_avatar_filename = f'avatars/{user.id}_predefined_{avatar_id}.png'
            user_avatar_path = Path(settings.MEDIA_ROOT) / user_avatar_filename
            user_avatar_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(predefined_path, user_avatar_path)
            user.avatar = user_avatar_filename

    user.save()

    return Response({
        'message': 'Username set successfully',
        'user': UserSerializer(user, context={'request': request}).data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def available_avatars(request):
    """Return list of available predefined avatars"""
    avatars = [
        {'id': 'av1', 'name': 'Avatar 1'},
        {'id': 'av2', 'name': 'Avatar 2'},
        {'id': 'av3', 'name': 'Avatar 3'},
        {'id': 'av4', 'name': 'Avatar 4'},
        {'id': 'av5', 'name': 'Avatar 5'},
        {'id': 'av6', 'name': 'Avatar 6'},
        {'id': 'av7', 'name': 'Avatar 7'},
        {'id': 'av8', 'name': 'Avatar 8'},
        {'id': 'av9', 'name': 'Avatar 9'},
        {'id': 'av10', 'name': 'Avatar 10'},
    ]

    # Add full URL to each avatar
    for avatar in avatars:
        avatar['url'] = request.build_absolute_uri(f'/api/users/predefined-avatar/{avatar["id"]}.png')

    return Response({'avatars': avatars}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def serve_predefined_avatar(request, filename):
    """Serve predefined avatar files from static_assets"""
    from django.http import FileResponse, Http404
    from pathlib import Path

    avatar_path = Path(settings.BASE_DIR) / 'static_assets' / 'avatars' / 'predefined' / filename

    if not avatar_path.exists():
        raise Http404("Avatar not found")

    return FileResponse(open(avatar_path, 'rb'), content_type='image/png')


@api_view(['GET'])
@permission_classes([AllowAny])
def serve_user_avatar(request, filename):
    """Serve user-uploaded avatar files from media volume"""
    from django.http import FileResponse, Http404
    from pathlib import Path
    import mimetypes

    avatar_path = Path(settings.MEDIA_ROOT) / 'avatars' / filename

    if not avatar_path.exists():
        raise Http404("Avatar not found")

    # Detect content type based on file extension
    content_type, _ = mimetypes.guess_type(str(avatar_path))
    if not content_type:
        content_type = 'application/octet-stream'

    return FileResponse(open(avatar_path, 'rb'), content_type=content_type)
