from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Level(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, default='General')
    difficulty = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
            ('expert', 'Expert'),
        ],
        default='beginner'
    )
    xp_reward = models.IntegerField(default=100)
    passing_percentage = models.IntegerField(default=70)
    level_number = models.IntegerField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['level_number']

    def __str__(self):
        return self.title


class Question(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()
    options = models.JSONField(default=list)
    correct_answer = models.IntegerField()
    explanation = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['level', 'id']

    def __str__(self):
        return self.question[:50]


class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress')
    current_level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    total_xp = models.IntegerField(default=0)
    completed_levels = models.ManyToManyField(Level, related_name='completed_by', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.total_xp} XP"


class QuizSubmission(models.Model):
    RESULT_CHOICES = [
        ('passed', 'Passed'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_submissions')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='submissions')
    answers = models.JSONField(default=list)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    percentage = models.FloatField()
    result = models.CharField(max_length=10, choices=RESULT_CHOICES)
    xp_earned = models.IntegerField(default=0)

    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        unique_together = [['user', 'level']]

    def __str__(self):
        return f"{self.user.email} - Level {self.level.title} - {self.result}"
