from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic as views

from budget_tracker.accounts.forms import RegistrationForm

UserModel = get_user_model()


class AccountCreateView(views.CreateView):
    model = UserModel
    template_name = 'accounts/account-create-page.html'
    form_class = RegistrationForm
