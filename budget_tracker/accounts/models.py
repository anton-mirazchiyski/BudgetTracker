from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


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

    first_name = models.CharField(max_length=150, blank=False, null=False)

    last_name = models.CharField(max_length=150, blank=False, null=False)

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


class UserProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Currency(models.Model):
    EURO = '€ EUR'
    DOLLAR = '$ USD'
    BRITISH_POUND = '£ GBP'

    CURRENCY_CHOICES = (
        (EURO, EURO),
        (DOLLAR, DOLLAR),
        (BRITISH_POUND, BRITISH_POUND),
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
