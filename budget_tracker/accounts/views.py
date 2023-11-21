from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import generic as views

from budget_tracker.accounts.forms import RegistrationForm, LoginForm

UserModel = get_user_model()


class AccountCreateView(views.CreateView):
    model = UserModel
    template_name = 'accounts/account-create-page.html'
    form_class = RegistrationForm


def login_user(request):
    if request.method == 'GET':
        login_form = LoginForm()
    else:
        login_form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('common:home')
        else:
            messages.error(request, 'Invalid email or password. '
                                    'Please try again.')
    return render(
        request,
        'accounts/account-login-page.html',
        {'form': login_form}
    )


def logout_user(request):
    logout(request)
    return redirect('common:home')
