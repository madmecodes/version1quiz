from django.urls import path
from . import views

urlpatterns = [
    path('', views.LeaderboardListView.as_view(), name='leaderboard_list'),
    path('user-rank/', views.user_rank, name='user_rank'),
    path('update/', views.update_leaderboard, name='update_leaderboard'),
    path('top/', views.top_leaderboard, name='top_leaderboard'),
]
