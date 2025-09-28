from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.open_settings, name='settings'),
]