from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]