from calendar import month_name
from datetime import datetime

from budget_tracker.accounts.models import Balance
from budget_tracker.expenses.models import Expense
from budget_tracker.income.models import Income


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


def calculate_income_over_the_months(profile):
    all_income = Income.objects.filter(profile=profile).order_by('date')
    all_expenses = Expense.objects.filter(profile=profile).order_by('date')

    months = []
    income_amounts = []
    expense_amounts = []

    for income in all_income:
        current_month = income.date.month
        if current_month not in months:
            months.append(current_month)

        amount_per_month = sum([income.amount for income in all_income if income.date.month == current_month])
        if amount_per_month not in income_amounts:
            income_amounts.append(amount_per_month)

        amount_of_expense_per_month = sum([expense.amount for expense in all_expenses
                                           if expense.date.month == current_month])
        if amount_of_expense_per_month not in expense_amounts:
            expense_amounts.append(amount_of_expense_per_month)

    months = [month_name[month] for month in months]
    return months, income_amounts, expense_amounts
