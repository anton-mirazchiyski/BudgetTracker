from django.core.validators import MinValueValidator
from django.db import models

from budget_tracker.accounts.models import UserProfile


class Income(models.Model):
    source = models.CharField(max_length=30, null=False, blank=False)

    amount = models.FloatField(validators=[MinValueValidator(0)], null=False, blank=False)

    submitted_on = models.DateTimeField(auto_now_add=True)

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)