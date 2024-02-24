from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from budget_tracker.accounts.forms import RegistrationForm, LoginForm, DetailsForm, CurrencyForm
from budget_tracker.accounts.models import UserProfile, Currency
from budget_tracker.core.currencies_utils import change_existing_currency, create_new_currency

UserModel = get_user_model()


class AccountCreateView(SuccessMessageMixin, views.CreateView):
    model = UserModel
    template_name = 'accounts/account-create-page.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('accounts:login-account')

    success_message = 'Your account was created. You can log in.'

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.create_profile_and_currency()
        return HttpResponseRedirect(super().get_success_url())

    def create_profile_and_currency(self):
        new_user_profile = UserProfile.objects.create(user=self.object, user_id=self.object.pk)
        new_user_profile.save()
        user_currency = Currency.objects.create(user_profile=new_user_profile)
        user_currency.save()


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
        currency_form = CurrencyForm(request)
    else:
        currency_form = CurrencyForm(request, request.POST)
        if currency_form.is_valid():
            new_currency = currency_form.save(commit=False)
            user_profile = UserProfile.objects.filter(user=user).get()
            has_old_currency = Currency.objects.filter(user_profile=user_profile).exists()

            if has_old_currency:
                change_existing_currency(user_profile, new_currency)

            if not has_old_currency:
                create_new_currency(request, user_profile)

            return redirect(request.META['HTTP_REFERER'])
    try:
        user_profile = UserProfile.objects.select_related('currency').filter(user_id=pk).get()
        current_currency = user_profile.currency
    except Currency.DoesNotExist:
        current_currency = Currency.EURO
    return render(request,
                  'currencies/currency-change-page.html',
                  {'form': currency_form, 'profile_pk': pk, 'currency': current_currency})
