from django.shortcuts import render
from django.views import generic as views

from budget_tracker.core.accounts_utils import get_user_profile
from budget_tracker.core.common_utils import get_recent_transactions
from budget_tracker.income.models import Income


class IndexView(views.TemplateView):
    template_name = 'common/home-page.html'


def month_mapper():
    month_names = {
        1: 'January',
        2: 'February',
        3: 'March',
    }
    return month_names


def show_dashboard(request):
    profile = get_user_profile(request)
    all_income = Income.objects.filter(profile=profile).order_by('date')
    months = []
    amounts = []

    for income in all_income:
        current_month = income.date.month
        if current_month not in months:
            months.append(current_month)
        amount_per_month = sum([income.amount for income in all_income if income.date.month == current_month])
        if amount_per_month not in amounts:
            amounts.append(amount_per_month)

    months = [month_mapper()[month] for month in months]

    labels = months
    data = [int(amount) for amount in amounts]

    context = {'labels': labels, 'data': data}

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
