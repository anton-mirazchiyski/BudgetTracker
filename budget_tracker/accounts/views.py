from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.views import generic as views

from budget_tracker.accounts.forms import RegistrationForm, LoginForm

UserModel = get_user_model()


class AccountCreateView(views.CreateView):
    model = UserModel
    template_name = 'accounts/account-create-page.html'
    form_class = RegistrationForm


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/account-login-page.html'
    authentication_form = LoginForm
