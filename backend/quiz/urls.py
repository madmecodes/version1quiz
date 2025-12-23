from django.urls import path
from . import views

urlpatterns = [
    path('levels/', views.LevelListView.as_view(), name='level_list'),
    path('levels/<int:id>/', views.LevelDetailView.as_view(), name='level_detail'),
    path('levels/<int:level_id>/questions/', views.level_questions, name='level_questions'),
    path('progress/', views.user_progress, name='user_progress'),
    path('submit/', views.submit_quiz, name='submit_quiz'),
    path('submission/<int:level_id>/', views.submission_detail, name='submission_detail'),
]
