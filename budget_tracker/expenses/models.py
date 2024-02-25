from django.db import models

from budget_tracker.accounts.models import UserProfile


class Expense(models.Model):
    description = models.TextField(null=True, blank=True)

    date = models.DateField(null=False, blank=False)

    amount = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)

    currency = models.CharField(max_length=30, null=False, blank=True)

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
