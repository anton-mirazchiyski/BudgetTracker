from django.core.exceptions import ValidationError


def validate_name_contains_only_letters(name):
    if not name.isalpha():
        raise ValidationError("Enter a valid name")


def validate_name_has_enough_length(name):
    minimum_length = 3
    if len(name) < minimum_length:
        raise ValidationError("Enter a valid name")
