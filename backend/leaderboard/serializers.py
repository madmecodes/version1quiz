from rest_framework import serializers
from django.contrib.auth import get_user_model
from quiz.models import UserProgress

User = get_user_model()


class UserProgressLeaderboardSerializer(serializers.ModelSerializer):
    """Serializes UserProgress for leaderboard display with dynamic rank calculation"""
    user_email = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    user_avatar = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    rank = serializers.SerializerMethodField()
    current_level_number = serializers.SerializerMethodField()

    class Meta:
        model = UserProgress
        fields = ['user_id', 'rank', 'user_email', 'username', 'user_avatar', 'total_xp', 'current_level_number', 'completed_levels', 'updated_at']

    def get_user_id(self, obj):
        return obj.user.id

    def get_user_email(self, obj):
        return obj.user.email

    def get_username(self, obj):
        return obj.user.username or obj.user.email

    def get_user_avatar(self, obj):
        if obj.user.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.user.avatar.url)
            return obj.user.avatar.url
        return None

    def get_current_level_number(self, obj):
        return obj.current_level.level_number if obj.current_level else 1

    def get_rank(self, obj):
        """Calculate rank dynamically based on current ordering"""
        all_users = self.context.get('all_users', [])
        if not all_users:
            return None
        try:
            return list(all_users).index(obj) + 1
        except ValueError:
            return None


# Keep old name for backward compatibility
LeaderboardSerializer = UserProgressLeaderboardSerializer
