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


def sum_transaction_amount_for_month(current_month, queryset):
    amount_for_month = sum([transaction.amount for transaction in queryset
                            if transaction.date.month == current_month])
    return amount_for_month


def get_total_amount_of_income_for_month(profile, month):
    all_income = Income.objects.filter(profile=profile).order_by('date')
    amount = sum_transaction_amount_for_month(month, all_income)
    return amount


def get_total_amount_of_expense_for_month(profile, month):
    all_expenses = Expense.objects.filter(profile=profile).order_by('date')
    amount = sum_transaction_amount_for_month(month, all_expenses)
    return amount


def get_all_months_of_transactions(profile):
    all_income = Income.objects.filter(profile=profile).order_by('date')
    all_expenses = Expense.objects.filter(profile=profile).order_by('date')

    months_of_income = [income.date.month for income in all_income]
    months_of_expenses = [expense.date.month for expense in all_expenses]
    all_months = set(months_of_income + months_of_expenses)

    return all_months


def get_chart_data(profile):
    all_months = get_all_months_of_transactions(profile)

    months = []
    income_amounts = []
    expense_amounts = []

    for month in all_months:
        months.append(month)

        income_amount = get_total_amount_of_income_for_month(profile, month)
        income_amounts.append(income_amount)

        expense_amount = get_total_amount_of_expense_for_month(profile, month)
        expense_amounts.append(expense_amount)

    months = [month_name[month] for month in months]

    return months, income_amounts, expense_amounts


def get_doughnut_chart_data(profile):
    all_months = get_all_months_of_transactions(profile)
    all_earned_income = profile.income_set.filter(type='Earned Income')
    all_passive_income = profile.income_set.filter(type='Passive Income')

    months = []
    earned_income = []
    passive_income = []

    for month in all_months:
        months.append(month)
        earned_income_amount_for_month = sum(
            [income.amount for income in all_earned_income if income.date.month == month])
        earned_income.append(earned_income_amount_for_month)

        passive_income_amount_for_month = sum(
            [income.amount for income in all_passive_income if income.date.month == month])
        passive_income.append(passive_income_amount_for_month)

    months = [month_name[month] for month in months]

    return months, earned_income, passive_income
