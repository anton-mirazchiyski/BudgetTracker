from django.contrib import admin
from budget_tracker.accounts.models import BudgetTrackerUser, UserProfile, Currency


class CustomUserAdmin(admin.ModelAdmin):
    fields = (['first_name', 'last_name', 'email', 'password'] +
              ['last_login', 'is_active', 'is_admin'])

    list_display = ['first_name', 'last_name', 'email']


admin.site.register(BudgetTrackerUser, CustomUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']

    @staticmethod
    def first_name(obj):
        return obj.user.first_name

    @staticmethod
    def last_name(obj):
        return obj.user.last_name

    @staticmethod
    def email(obj):
        return obj.user.email


admin.site.register(UserProfile, UserProfileAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'currency']


admin.site.register(Currency, CurrencyAdmin)
