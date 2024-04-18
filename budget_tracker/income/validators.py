from django.core.exceptions import ValidationError


def validate_income_source_contains_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Income source must contain only letters.')
