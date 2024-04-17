from django.core.exceptions import ValidationError


def validate_name_contains_only_letters(name):
    if not name.isalpha():
        raise ValidationError('Enter a valid name')


def validate_name_starts_with_capital_letter(name):
    if not name[0].isupper():
        raise ValidationError('A name must start with a capital letter')
