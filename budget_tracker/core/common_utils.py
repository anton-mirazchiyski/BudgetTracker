from datetime import datetime

from budget_tracker.accounts.models import Balance


def get_current_balance(profile):
    current_balance = Balance.objects.filter(user_profile=profile).get()
    return current_balance


def add_to_balance(profile, amount):
    balance = get_current_balance(profile)
    balance.amount += amount
    balance.save()


def subtract_from_balance(profile, amount):
    balance = get_current_balance(profile)
    balance.amount -= amount
    balance.save()


def get_recent_transactions(profile):
    all_income = profile.income_set.all()
    all_expenses = profile.expense_set.all()
    all_transactions = list(all_income) + list(all_expenses)
    sorted_transactions = sorted(all_transactions, key=lambda x: x.created_at, reverse=True)[:4]
    return sorted_transactions


def get_current_month():
    current_month = datetime.today().month
    return current_month
