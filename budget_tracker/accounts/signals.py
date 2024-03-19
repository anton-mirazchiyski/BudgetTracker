from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from budget_tracker.accounts.models import UserProfile, Currency, Balance

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=UserProfile)
def create_currency(sender, instance, created, **kwargs):
    if created:
        Currency.objects.create(user_profile=instance)


@receiver(post_save, sender=UserProfile)
def start_balance(sender, instance, created, **kwargs):
    if created:
        Balance.objects.create(user_profile=instance, amount=0, currency=instance.currency)
