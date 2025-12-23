from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio', 'total_xp', 'current_level', 'rank']
        read_only_fields = ['total_xp', 'current_level', 'rank']


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'avatar', 'profile']
        read_only_fields = ['id', 'email']

    def get_avatar(self, obj):
        if obj.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.avatar.url)
            return obj.avatar.url
        return None


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    username = serializers.CharField(required=False, allow_blank=False)
    avatar = serializers.ImageField(required=False)
    avatar_id = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'avatar', 'avatar_id']

    def validate_username(self, value):
        if value:
            user = self.context['request'].user
            if User.objects.filter(username=value).exclude(id=user.id).exists():
                raise serializers.ValidationError("Username already exists.")
        return value

    def save(self, **kwargs):
        # Handle predefined avatar_id
        avatar_id = self.validated_data.get('avatar_id')
        if avatar_id:
            import shutil
            from pathlib import Path
            from django.conf import settings

            predefined_path = Path(settings.MEDIA_ROOT) / 'avatars' / 'predefined' / f'{avatar_id}.png'
            if predefined_path.exists():
                user_avatar_filename = f'avatars/{self.instance.id}_predefined_{avatar_id}.png'
                user_avatar_path = Path(settings.MEDIA_ROOT) / user_avatar_filename
                user_avatar_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(predefined_path, user_avatar_path)
                self.instance.avatar = user_avatar_filename

            # Remove avatar_id from validated_data so it doesn't try to save to model
            self.validated_data.pop('avatar_id', None)

        instance = super().save(**kwargs)
        return instance


class GoogleAuthSerializer(serializers.Serializer):
    access_token = serializers.CharField()


class UsernameCheckSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=150)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value
