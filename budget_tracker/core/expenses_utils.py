from budget_tracker.core.common_utils import add_to_balance


def delete_expense(profile, expense, choice):
    if choice == 'Delete WITH money returning to balance':
        add_to_balance(profile, expense.amount)
    expense.delete()
