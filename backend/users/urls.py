from django.urls import path
from . import views

urlpatterns = [
    path('auth/google/', views.google_oauth_callback, name='google_oauth'),
    path('profile/', views.user_profile, name='user_profile'),
    path('check-username/', views.check_username, name='check_username'),
    path('set-username/', views.set_username, name='set_username'),
    path('available-avatars/', views.available_avatars, name='available_avatars'),
    path('predefined-avatar/<str:filename>', views.serve_predefined_avatar, name='serve_predefined_avatar'),
]
