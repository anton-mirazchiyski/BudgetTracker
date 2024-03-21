from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from budget_tracker.accounts.models import Currency, UserProfile

UserModel = get_user_model()


class AccountsBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-input registration-form-input'

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'password')

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First name',

                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last name',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                }
            )
        }


class RegistrationForm(AccountsBaseForm):

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Confirm Password'}),
        label='Password')

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(AccountsBaseForm):
    class Meta(AccountsBaseForm.Meta):
        fields = ('email', 'password')


class DetailsForm(AccountsBaseForm):
    class Meta(AccountsBaseForm.Meta):
        fields = ('first_name', 'last_name', 'email')


class CurrencyForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)
        user_profile = (UserProfile.objects.select_related('currency').
                        filter(user=self.request.user).get())
        try:
            user_currency = user_profile.currency
        except Currency.DoesNotExist:
            user_currency = Currency.EURO
        self.fields['currency'].initial = user_currency

    class Meta:
        model = Currency
        fields = ('currency',)

        widgets = {
            'currency': forms.Select(
                attrs={
                    'class': 'currency-form-input form-input'
                }
            )
        }
