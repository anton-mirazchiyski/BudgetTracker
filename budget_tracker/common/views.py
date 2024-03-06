from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import generic as views

from budget_tracker.core.accounts_utils import get_user_profile


def index(request):
    try:
        current_user_profile = request.user
        profile_pk = current_user_profile.pk
    except ObjectDoesNotExist:
        current_user_profile, profile_pk = None, None

    return render(
        request,
        'common/home-page.html',
        {'profile_pk': profile_pk}
    )


def show_balance(request):
    profile = get_user_profile(request)
    balance = profile.balance
    context = {'balance': balance}

    return render(request,'common/balance-page.html', context)
