from django.contrib import admin
from .models import Level, Question, UserProgress, QuizSubmission


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('level_number', 'title', 'difficulty', 'xp_reward', 'passing_percentage')
    list_filter = ('difficulty', 'level_number')
    search_fields = ('title', 'description')
    ordering = ('level_number',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'level', 'question')
    list_filter = ('level',)
    search_fields = ('question',)


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_level', 'total_xp')
    list_filter = ('current_level', 'total_xp')
    search_fields = ('user__email', 'user__username')


@admin.register(QuizSubmission)
class QuizSubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'result', 'percentage', 'xp_earned', 'submitted_at')
    list_filter = ('result', 'level', 'submitted_at')
    search_fields = ('user__email', 'level__title')
    readonly_fields = ('submitted_at',)
