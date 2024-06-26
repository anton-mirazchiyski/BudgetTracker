from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from budget_tracker.accounts.validators import validate_name_contains_only_letters, \
    validate_name_starts_with_capital_letter


class MyCustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class BudgetTrackerUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)

    first_name = models.CharField(max_length=50,
                                  validators=[
                                        validate_name_contains_only_letters,
                                        validate_name_starts_with_capital_letter,
                                        MinLengthValidator(3, message='A name must contain at least 3 letters'),
                                  ],
                                  blank=False, null=False)

    last_name = models.CharField(max_length=50,
                                 validators=[
                                     validate_name_contains_only_letters,
                                     validate_name_starts_with_capital_letter,
                                     MinLengthValidator(3, message='A name must contain at least 3 letters'),
                                 ],
                                 blank=False, null=False)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    objects = MyCustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


UserModel = get_user_model()


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.user_profile.user.pk}/{filename}'


class UserProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Currency(models.Model):
    EURO = '€ EUR'
    DOLLAR = '$ USD'
    BRITISH_POUND = '£ GBP'
    BULGARIAN_LEV = 'лв BGN'

    CURRENCY_CHOICES = (
        (EURO, EURO),
        (DOLLAR, DOLLAR),
        (BRITISH_POUND, BRITISH_POUND),
        (BULGARIAN_LEV, BULGARIAN_LEV),
    )

    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        default=EURO,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.currency


class Balance(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    amount = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=False, blank=False
    )

    currency = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Balance'

    def __str__(self):
        return f'{self.currency} {self.amount}'

    def save(self, *args, **kwargs):
        if self.amount < 0:
            self.amount = 0
        super(Balance, self).save(*args, **kwargs)


class ProfilePhoto(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    photo = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return f'Photo of {self.user_profile}'
