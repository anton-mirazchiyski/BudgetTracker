from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from budget_tracker.accounts.forms import RegistrationForm, LoginForm, CurrencyForm, ProfilePhotoForm
from budget_tracker.accounts.models import Currency, ProfilePhoto
from budget_tracker.core.accounts_utils import get_user_profile, get_profile_photo
from budget_tracker.core.common_utils import get_current_balance
from budget_tracker.core.currencies_utils import change_existing_currency, get_current_currency

UserModel = get_user_model()


class AccountCreateView(SuccessMessageMixin, views.CreateView):
    model = UserModel
    template_name = 'accounts/account-create-page.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('accounts:login-account')

    success_message = 'Your account was created. You can log in.'


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
            return redirect('common:dashboard')
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


def show_profile_details(request, pk):
    profile = get_user_profile(request)
    if request.method == 'POST':
        form = ProfilePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            previous_photo = get_profile_photo(profile)
            if previous_photo is not None:
                previous_photo.delete()
            form.user_profile = profile
            form.save()
            return redirect('accounts:details-profile', pk)
    form = ProfilePhotoForm()

    photo = get_profile_photo(profile)
    balance = get_current_balance(profile)
    context = {
        'form': form,
        'profile': profile,
        'photo': photo,
        'balance': balance,
    }
    return render(
        request,
        'accounts/account-details-page.html',
        context
    )


def delete_profile_photo(request, pk):
    profile = get_user_profile(request)
    photo = ProfilePhoto.objects.filter(user_profile=profile).get()
    photo.delete()
    return redirect('accounts:details-profile', pk)


def change_currency(request, pk):
    user_profile = get_user_profile(request)

    if request.method == 'POST':
        currency_form = CurrencyForm(request, request.POST)
        if currency_form.is_valid():
            new_currency = currency_form.save(commit=False)
            has_old_currency = Currency.objects.filter(user_profile=user_profile).exists()

            if has_old_currency:
                change_existing_currency(user_profile, new_currency)
            new_currency.save()
            return redirect(request.META['HTTP_REFERER'])

    currency_form = CurrencyForm(request)
    current_currency = get_current_currency(request)
    context = {
        'form': currency_form,
        'currency': current_currency
    }

    return render(
        request,
        'currencies/currency-change-page.html',
        context
    )


class AccountDeleteView(views.TemplateView):
    template_name = 'accounts/account-delete-page.html'


def delete_user_data(request, pk):
    current_user = UserModel.objects.filter(pk=pk).get()
    current_user.delete()
    return redirect('common:home')
