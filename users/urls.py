from django.urls import path, include
from django.contrib.auth import views as auth_views

from users import views
from .views import RegisterView, open_users

urlpatterns = [
    path('', views.open_users, name='users'),
    
    # кастомный password reset
    path('accounts/password_reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),

    # стандартные auth urls
    path('accounts/', include('django.contrib.auth.urls')),

    path('register/', views.RegisterView.as_view(), name='register'),
]
