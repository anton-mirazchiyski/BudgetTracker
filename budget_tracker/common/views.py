from django.shortcuts import render
from django.views import generic as views

from budget_tracker.core.accounts_utils import get_user_profile
from budget_tracker.core.common_utils import get_recent_transactions, get_primary_chart_data, get_secondary_chart_data
from budget_tracker.core.currencies_utils import get_current_currency


class IndexView(views.TemplateView):
    template_name = 'common/index.html'


def show_dashboard(request):
    profile = get_user_profile(request)
    months, income_amounts, expense_amounts = get_primary_chart_data(profile)
    months, earned_income, passive_income = get_secondary_chart_data(profile)

    labels = months
    data = [int(amount) for amount in income_amounts]
    data2 = [int(amount) for amount in expense_amounts]
    currency = get_current_currency(request)

    earned_income_data = [int(amount) for amount in earned_income]
    passive_income_data = [int(amount) for amount in passive_income]

    context = {
        'labels': labels,
        'data': data,
        'data2': data2,
        'currency': currency,
        'earned_income_data': earned_income_data,
        'passive_income_data': passive_income_data,
    }

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
