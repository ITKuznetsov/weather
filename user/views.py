from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

from common.views import TitleMixin
from user.forms import UserLoginForm, UserRegistrationForm


class UserLoginView(TitleMixin, LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('user:login')
    success_message = 'Регистрация прошла успешно!'
    title = 'Регистрация'