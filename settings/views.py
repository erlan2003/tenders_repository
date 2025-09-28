from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q

def open_settings(request):
    return render(request, 'settings.html')