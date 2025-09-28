from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.open_users, name='users'),
]