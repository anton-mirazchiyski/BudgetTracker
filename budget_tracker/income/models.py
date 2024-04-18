from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from datetime import date

from budget_tracker.accounts.models import UserProfile, Currency
from budget_tracker.income.validators import validate_income_source_contains_only_letters


class Income(models.Model):

    MIN_LEN_INCOME_SOURCE = 4
    MIN_AMOUNT = 5

    EARNED_INCOME = 'Earned Income'
    PASSIVE_INCOME = 'Passive Income'
    PORTFOLIO_INCOME = 'Portfolio Income'

    INCOME_CHOICES = (
        (EARNED_INCOME, EARNED_INCOME),
        (PASSIVE_INCOME, PASSIVE_INCOME),
        (PORTFOLIO_INCOME, PORTFOLIO_INCOME),
    )

    income_source_error_message = f'Income source must contain at least {MIN_LEN_INCOME_SOURCE} characters'
    amount_error_message = f'Minimum amount must be greater than {MIN_AMOUNT}'

    source = models.CharField(max_length=30,
                              validators=[MinLengthValidator(MIN_LEN_INCOME_SOURCE,
                                                             message=income_source_error_message),
                                          validate_income_source_contains_only_letters],
                              null=False, blank=False)

    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 validators=[MinValueValidator(MIN_AMOUNT, message=amount_error_message)],
                                 null=False, blank=False)

    type = models.CharField(max_length=30, choices=INCOME_CHOICES, null=False, blank=False)

    currency = models.CharField(max_length=30, null=True, blank=True)

    date = models.DateField(default=date.today, null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount}{self.currency} - {self.date}'
