from budget_tracker.accounts.models import Currency
from budget_tracker.core.accounts_utils import get_user_profile


def change_existing_currency(user_profile, new_currency):
    old_currency = Currency.objects.filter(user_profile=user_profile).get()
    old_currency.delete()
    user_profile.currency = new_currency


def get_current_currency(request):
    profile = get_user_profile(request)
    current_currency = profile.currency
    return current_currency
