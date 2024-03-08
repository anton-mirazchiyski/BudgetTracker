from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import generic as views

from budget_tracker.core.accounts_utils import get_user_profile
from budget_tracker.core.common_utils import get_recent_transactions


class IndexView(views.TemplateView):
    template_name = 'common/home-page.html'


def show_balance(request):
    profile = get_user_profile(request)
    balance = profile.balance
    transactions = get_recent_transactions(profile)
    context = {
        'balance': balance,
        'transactions': transactions
    }

    return render(request,'common/balance-page.html', context)
