from django.contrib.auth.views import LoginView
from django.views.generic.base import View, TemplateView

from .forms import MyRegistrationForm
from django.shortcuts import render, redirect


class MyRegistrationView(View):
    def get(self, request):
        return render(request, 'users/registration.html', context={'form': MyRegistrationForm})

    def post(self, request, *args, **kwargs):
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'users/registration.html', context={'form': form})


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'


class ProfileView(TemplateView):
    template_name = 'users/profile.html'
