from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.open_my_requets, name='my_requests'),
]