from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import F

from .models import Level, Question, UserProgress, QuizSubmission
from .serializers import (
    LevelSerializer,
    LevelDetailSerializer,
    QuestionSerializer,
    UserProgressSerializer,
    QuizSubmissionSerializer,
    QuizSubmitSerializer
)


class LevelListView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [AllowAny]


class LevelDetailView(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def level_questions(request, level_id):
    level = get_object_or_404(Level, id=level_id)
    questions = level.questions.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_progress(request):
    user = request.user

    # Get or create progress with Level 1 as default
    first_level = Level.objects.filter(level_number=1).first()
    progress, created = UserProgress.objects.get_or_create(
        user=user,
        defaults={
            'current_level': first_level,
            'total_xp': 0,
        }
    )

    serializer = UserProgressSerializer(progress)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_quiz(request):
    user = request.user
    serializer = QuizSubmitSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    level_id = serializer.validated_data['level_id']
    answers = serializer.validated_data['answers']

    level = get_object_or_404(Level, id=level_id)
    questions = level.questions.all().order_by('id')

    if questions.count() != len(answers):
        return Response(
            {'error': 'Answer count mismatch'},
            status=status.HTTP_400_BAD_REQUEST
        )

    correct_count = 0
    for question, answer in zip(questions, answers):
        if answer == question.correct_answer:
            correct_count += 1

    percentage = round((correct_count / len(answers)) * 100, 2)
    passed = percentage >= level.passing_percentage
    xp_earned = level.xp_reward if passed else 0

    submission, created = QuizSubmission.objects.get_or_create(
        user=user,
        level=level,
        defaults={
            'answers': answers,
            'score': correct_count,
            'total_questions': len(answers),
            'percentage': percentage,
            'result': 'passed' if passed else 'failed',
            'xp_earned': xp_earned,
        }
    )

    if not created:
        submission.answers = answers
        submission.score = correct_count
        submission.total_questions = len(answers)
        submission.percentage = percentage
        submission.result = 'passed' if passed else 'failed'
        submission.xp_earned = xp_earned
        submission.save()

    # Get or create progress with Level 1 as default
    first_level = Level.objects.filter(level_number=1).first()
    progress, _ = UserProgress.objects.get_or_create(
        user=user,
        defaults={
            'current_level': first_level,
            'total_xp': 0,
        }
    )

    if passed and level not in progress.completed_levels.all():
        progress.completed_levels.add(level)
        progress.total_xp = F('total_xp') + xp_earned
        progress.save()
        progress.refresh_from_db()

    # Update current_level to the next level after the highest completed
    if passed:
        completed_level_numbers = progress.completed_levels.values_list('level_number', flat=True)
        if completed_level_numbers:
            max_completed = max(completed_level_numbers)
            next_level = Level.objects.filter(level_number=max_completed + 1).first()
            current_level_num = progress.current_level.level_number if progress.current_level else 0
            if next_level and current_level_num <= max_completed:
                progress.current_level = next_level
                progress.save()
                progress.refresh_from_db()

    # Leaderboard rank is calculated dynamically from UserProgress
    # No need to manually update leaderboard table

    return Response({
        'submission': QuizSubmissionSerializer(submission).data,
        'passed': passed,
        'percentage': percentage,
        'xp_earned': xp_earned,
        'progress': UserProgressSerializer(progress).data,
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def submission_detail(request, level_id):
    user = request.user
    submission = get_object_or_404(QuizSubmission, user=user, level_id=level_id)
    level = submission.level
    questions = level.questions.all().order_by('id')

    serializer = QuizSubmissionSerializer(submission)
    return Response({
        'submission': serializer.data,
        'questions': [
            {
                'id': q.id,
                'question': q.question,
                'options': q.options,
                'correct_answer': q.correct_answer,
                'user_answer': submission.answers[i] if i < len(submission.answers) else None,
                'explanation': q.explanation,
            }
            for i, q in enumerate(questions)
        ]
    })
