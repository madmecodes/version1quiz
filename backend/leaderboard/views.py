from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from django.db.models import Count

from .serializers import LeaderboardSerializer
from quiz.models import UserProgress, QuizSubmission


class LeaderboardPagination(PageNumberPagination):
    page_size = 100


class LeaderboardListView(generics.ListAPIView):
    queryset = UserProgress.objects.all().order_by('-total_xp').distinct()
    serializer_class = LeaderboardSerializer
    pagination_class = LeaderboardPagination
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        # Pass all users for rank calculation
        context['all_users'] = list(self.get_queryset())
        return context


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_rank(request):
    user = request.user
    try:
        user_progress = UserProgress.objects.get(user=user)
    except UserProgress.DoesNotExist:
        avatar_url = None
        if user.avatar:
            avatar_url = request.build_absolute_uri(user.avatar.url)

        return Response({
            'rank': None,
            'xp': 0,
            'level': 1,
            'user': {
                'email': user.email,
                'username': user.username or user.email,
                'avatar': avatar_url,
            }
        }, status=status.HTTP_200_OK)

    # Calculate rank
    all_users = UserProgress.objects.all().order_by('-total_xp').distinct()
    rank = None
    for i, up in enumerate(all_users, 1):
        if up.id == user_progress.id:
            rank = i
            break

    serializer = LeaderboardSerializer(
        user_progress,
        context={'request': request, 'all_users': list(all_users)}
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_leaderboard(request):
    """Updates user's progress in leaderboard (called after quiz submission)"""
    from quiz.models import Level

    user = request.user

    try:
        user_progress = UserProgress.objects.get(user=user)
    except UserProgress.DoesNotExist:
        # Create initial progress if missing
        first_level = Level.objects.filter(level_number=1).first()
        user_progress = UserProgress.objects.create(
            user=user,
            current_level=first_level,
            total_xp=0,
        )

    # Calculate rank
    all_users = UserProgress.objects.all().order_by('-total_xp').distinct()

    serializer = LeaderboardSerializer(
        user_progress,
        context={'request': request, 'all_users': list(all_users)}
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def top_leaderboard(request, limit=10):
    limit = int(request.query_params.get('limit', limit))
    all_users = UserProgress.objects.all().order_by('-total_xp').distinct()
    top_users = all_users[:limit]
    serializer = LeaderboardSerializer(
        top_users,
        many=True,
        context={'request': request, 'all_users': list(all_users)}
    )
    return Response(serializer.data, status=status.HTTP_200_OK)
