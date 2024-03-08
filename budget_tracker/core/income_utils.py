from budget_tracker.core.common_utils import get_current_month


def find_highest_income_for_the_month(profile):
    current_month = get_current_month()

    highest_income_amount = 0
    highest_income = None

    income_for_the_month = profile.income_set.filter(date__month=current_month)
    for income in income_for_the_month:
        if income.amount > highest_income_amount:
            highest_income_amount = income.amount
            highest_income = income

    return highest_income
