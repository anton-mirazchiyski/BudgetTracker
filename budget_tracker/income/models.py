from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from datetime import date

from budget_tracker.accounts.models import UserProfile, Currency
from budget_tracker.income.validators import validate_income_source_contains_only_letters


class Income(models.Model):

    MAX_LEN_INCOME_SOURCE = 30
    MIN_LEN_INCOME_SOURCE = 4
    MIN_AMOUNT = 5
    MAX_LEN_TYPE = 25
    MAX_LEN_CURRENCY = 10

    EARNED_INCOME = 'Earned Income'
    PASSIVE_INCOME = 'Passive Income'
    PORTFOLIO_INCOME = 'Portfolio Income'

    INCOME_CHOICES = (
        (EARNED_INCOME, EARNED_INCOME),
        (PASSIVE_INCOME, PASSIVE_INCOME),
        (PORTFOLIO_INCOME, PORTFOLIO_INCOME),
    )

    income_source_error_message = f'Income source must contain at least {MIN_LEN_INCOME_SOURCE} characters'
    amount_error_message = f'Minimum amount must be at least {MIN_AMOUNT}'

    source = models.CharField(max_length=MAX_LEN_INCOME_SOURCE,
                              validators=[MinLengthValidator(MIN_LEN_INCOME_SOURCE,
                                                             message=income_source_error_message),
                                          validate_income_source_contains_only_letters],
                              null=False, blank=False)

    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 validators=[MinValueValidator(MIN_AMOUNT, message=amount_error_message)],
                                 null=False, blank=False)

    type = models.CharField(max_length=MAX_LEN_TYPE, choices=INCOME_CHOICES, null=False, blank=False)

    currency = models.CharField(max_length=MAX_LEN_CURRENCY, null=True, blank=True)

    date = models.DateField(default=date.today, null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'Income - {self.amount}{self.currency} - {self.date}'
