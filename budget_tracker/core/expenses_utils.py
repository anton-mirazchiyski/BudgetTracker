from budget_tracker.core.common_utils import add_to_balance, get_current_balance, get_recent_transactions
from budget_tracker.income.models import Income


def add_penultimate_transaction_to_balance_if_is_income(profile):
    recent_transactions = get_recent_transactions(profile)[::-1]
    penultimate_transaction = recent_transactions[-2]
    if isinstance(penultimate_transaction, Income):
        add_to_balance(profile, penultimate_transaction.amount)


def determine_expense_return_amount_on_delete(profile, expense):
    current_balance = get_current_balance(profile)
    if current_balance.amount == 0:
        add_penultimate_transaction_to_balance_if_is_income(profile)
    else:
        add_to_balance(profile, expense.amount)
