from pyexpat.errors import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'main/home.html')