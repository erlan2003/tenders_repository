
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.db.models import Q
from django.views import View

from users.forms import UserCreationForm

def open_users(request):
    return render(request, 'users.html')

class RegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form' : UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('login')
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)
        