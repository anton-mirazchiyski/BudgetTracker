from django.contrib import admin
from budget_tracker.accounts.models import BudgetTrackerUser


class CustomUserAdmin(admin.ModelAdmin):
    fields = (['first_name', 'last_name', 'email', 'password'] +
              ['last_login', 'is_active', 'is_admin'])

    list_display = ['first_name', 'last_name', 'email']


admin.site.register(BudgetTrackerUser, CustomUserAdmin)
