from rest_framework import serializers
from .models import Level, Question, UserProgress, QuizSubmission


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'options', 'explanation']


class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'options', 'correct_answer', 'explanation']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id', 'title', 'description', 'difficulty', 'xp_reward', 'passing_percentage', 'level_number', 'category']


class LevelDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Level
        fields = ['id', 'title', 'description', 'difficulty', 'xp_reward', 'passing_percentage', 'level_number', 'category', 'questions']


class UserProgressSerializer(serializers.ModelSerializer):
    current_level = LevelSerializer(read_only=True)
    completed_levels = LevelSerializer(many=True, read_only=True)
    level_progress = serializers.SerializerMethodField()

    class Meta:
        model = UserProgress
        fields = ['current_level', 'total_xp', 'completed_levels', 'level_progress']

    def get_level_progress(self, obj):
        """Build a dictionary of level progress based on quiz submissions"""
        submissions = QuizSubmission.objects.filter(user=obj.user).select_related('level')

        progress_dict = {}
        for submission in submissions:
            progress_dict[submission.level.level_number] = {
                'passed': submission.result == 'passed',
                'highest_score': submission.score,
                'total_questions': submission.total_questions,
                'percentage': submission.percentage,
            }

        return progress_dict


class QuizSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizSubmission
        fields = ['level', 'answers', 'score', 'total_questions', 'percentage', 'result', 'xp_earned', 'submitted_at']
        read_only_fields = ['score', 'percentage', 'result', 'xp_earned', 'submitted_at']


class QuizSubmitSerializer(serializers.Serializer):
    level_id = serializers.IntegerField()
    answers = serializers.ListField(child=serializers.IntegerField())

    def validate(self, data):
        from .models import Level
        try:
            level = Level.objects.get(id=data['level_id'])
        except Level.DoesNotExist:
            raise serializers.ValidationError("Level not found")

        question_count = level.questions.count()
        if len(data['answers']) != question_count:
            raise serializers.ValidationError(
                f"Expected {question_count} answers, got {len(data['answers'])}"
            )

        return data
