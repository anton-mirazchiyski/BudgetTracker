from django.shortcuts import render
from django.views import generic as views

from budget_tracker.core.accounts_utils import get_user_profile
from budget_tracker.core.common_utils import get_recent_transactions, calculate_income_over_the_months
from budget_tracker.core.currencies_utils import get_current_currency


class IndexView(views.TemplateView):
    template_name = 'common/home-page.html'


def show_dashboard(request):
    profile = get_user_profile(request)
    months, amounts = calculate_income_over_the_months(profile)

    labels = months
    data = [int(amount) for amount in amounts]
    currency = get_current_currency(request)

    context = {'labels': labels, 'data': data, 'currency': currency}

    return render(request, 'common/dashboard.html', context)


def show_balance(request):
    profile = get_user_profile(request)
    balance = profile.balance
    transactions = get_recent_transactions(profile)
    context = {
        'balance': balance,
        'transactions': transactions
    }

    return render(request,'common/balance-page.html', context)
