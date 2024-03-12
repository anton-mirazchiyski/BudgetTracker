from django.db import models
from datetime import date

from budget_tracker.accounts.models import UserProfile, Currency


class Income(models.Model):

    EARNED_INCOME = 'Earned Income'
    PASSIVE_INCOME = 'Passive Income'
    PORTFOLIO_INCOME = 'Portfolio Income'

    INCOME_CHOICES = (
        (EARNED_INCOME, EARNED_INCOME),
        (PASSIVE_INCOME, PASSIVE_INCOME),
        (PORTFOLIO_INCOME, PORTFOLIO_INCOME),
    )

    source = models.CharField(max_length=30, null=False, blank=False)

    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    type = models.CharField(max_length=30, choices=INCOME_CHOICES, null=False, blank=False)

    currency = models.CharField(max_length=30, null=True, blank=True)

    date = models.DateField(default=date.today, null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount}{self.currency} - {self.date}'
