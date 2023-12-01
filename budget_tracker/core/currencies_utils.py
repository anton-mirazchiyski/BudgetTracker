from budget_tracker.accounts.models import Currency, UserProfile


def change_existing_currency(user_profile, new_currency):
    old_currency = Currency.objects.filter(user_profile=user_profile).get()
    old_currency.delete()
    user_profile.currency = new_currency
    new_currency.save()


def create_new_currency(request, user_profile):
    new_value = request.POST['currency']
    new_currency = Currency.objects.create(user_profile=user_profile, currency=new_value)
    new_currency.save()


def get_current_currency(request):
    user = request.user
    user_profile = UserProfile.objects.select_related('currency').filter(user=user).get()
    current_currency = user_profile.currency
    return current_currency
