from django.urls import path
from account import views as users_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', users_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('profile/', users_views.profile,name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password_rest/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password-reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'),name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),


    
]
