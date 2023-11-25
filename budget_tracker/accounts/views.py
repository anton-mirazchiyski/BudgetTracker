from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import generic as views

from budget_tracker.accounts.forms import RegistrationForm, LoginForm, DetailsForm, CurrencyForm
from budget_tracker.accounts.models import UserProfile, Currency

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


def details_profile(request, pk):
    profile = UserModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = DetailsForm(instance=profile)
    else:
        form = DetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])
    return render(
        request,
        'accounts/account-details-page.html',
        {'form': form, 'profile_pk': pk}
    )


def change_currency(request, pk):
    user = request.user
    if request.method == 'GET':
        currency_form = CurrencyForm()
    else:
        currency_form = CurrencyForm(request.POST)
        if currency_form.is_valid():
            new_currency = currency_form.save(commit=False)
            user_profile = UserProfile.objects.filter(user=user).get()
            old_currency = Currency.objects.filter(user_profile=user_profile).get()
            if old_currency.currency != new_currency.currency:
                old_currency.delete()
                user_profile.currency = new_currency
                new_currency.save()

    return render(request,
                  'currencies/currency-change-page.html',
                  {'form': currency_form, 'profile_pk': pk})
