from django.views.generic.edit import FormView
from main.forms import RegisterForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'main/home.html')

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("login")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('/')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'main/edit_profile.html', {'form': form})


def profile_view(request):
    user = request.user
    try:
        donor = Donor.objects.get(user=user)
    except Donor.DoesNotExist:
        donor = None

    context = {
        'user': user,
        'donor': donor,
    }
    return render(request, 'profile.html', context)