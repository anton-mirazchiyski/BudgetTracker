from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from budget_tracker.accounts.models import UserProfile
from budget_tracker.income.models import Income


UserModel = get_user_model()


class IncomeModelTests(TestCase):

    INCOME_DATA = {
        'source': 'salary',
        'amount': 1000,
        'type': 'Earned Income',
        'currency': '€ EUR',
    }

    @staticmethod
    def get_user_profile():
        user = UserModel.objects.create_user(
            email='ivanov@yahoo.com',
            first_name='Ivan',
            last_name='Ivanov',
            password='ivanov1234'
        )
        user_profile = UserProfile.objects.get(user=user)
        return user_profile

    def test_income_create__when_valid_source__should_create_it(self):
        income = Income(**self.INCOME_DATA)
        income.profile = self.get_user_profile()

        income.full_clean()
        income.save()
        self.assertIsNotNone(income)

    def test_income_create__when_invalid_source__should_raise(self):
        invalid_source = '1st-salary'

        with self.assertRaises(ValidationError):
            income = Income(**self.INCOME_DATA)
            income.source = invalid_source
            income.profile = self.get_user_profile()

            income.full_clean()
            income.save()
