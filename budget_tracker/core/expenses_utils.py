from budget_tracker.core.common_utils import add_to_balance, get_current_balance


def determine_expense_return_amount_on_delete(profile, expense):
    current_balance = get_current_balance(profile)
    if current_balance.amount == 0:
        last_income = profile.income_set.last()
        if last_income:
            add_to_balance(profile, last_income.amount)
    else:
        add_to_balance(profile, expense.amount)


def delete_expense(profile, expense, choice):
    if choice == 'Delete WITH money returning to balance':
        determine_expense_return_amount_on_delete(profile, expense)

    expense.delete()
