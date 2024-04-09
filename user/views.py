from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from .models import MyUser
from .forms import UserRegisterForm, UserLoginForm


class SignUpView(CreateView):
    model = MyUser
    template_name = 'user/sign_up.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, username=phone_number, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})


def user_logout(request):

    logout(request)

    return redirect('index')
