from django.urls import include, path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
]