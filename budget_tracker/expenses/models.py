from django.db import models

from budget_tracker.accounts.models import UserProfile


class Expense(models.Model):
    description = models.TextField(null=True, blank=True)

    date = models.DateField(null=False, blank=False)

    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    currency = models.CharField(max_length=30, null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount}{self.currency} - {self.date}'
