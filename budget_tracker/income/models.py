from django.core.validators import MinValueValidator
from django.db import models

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

    amount = models.FloatField(validators=[MinValueValidator(0)], null=False, blank=False)

    type = models.CharField(max_length=30, choices=INCOME_CHOICES, null=False, blank=False)

    currency = models.CharField(max_length=30, null=True, blank=True)

    submitted_on = models.DateTimeField(auto_now_add=True)

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
