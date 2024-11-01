from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from budget_tracker.accounts.models import UserProfile


class Expense(models.Model):

    MAX_LEN_DESCRIPTION = 60
    MIN_LEN_DESCRIPTION = 5
    MIN_AMOUNT = 5

    description_error_message = f'Expense description must contain at least {MIN_LEN_DESCRIPTION} characters!'
    amount_error_message = f'Minimum amount must be at least {MIN_AMOUNT}'

    description = models.CharField(max_length=MAX_LEN_DESCRIPTION,
                                   validators=[MinLengthValidator(5, message=description_error_message)],
                                   null=False, blank=False)

    date = models.DateField(null=False, blank=False)

    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 validators=[MinValueValidator(MIN_AMOUNT, message=amount_error_message)],
                                 null=False, blank=False)

    currency = models.CharField(max_length=30, null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'Expense - {self.amount}{self.currency} - {self.date}'
