from django.contrib import admin

from budget_tracker.expenses.models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'currency', 'profile')


admin.site.register(Expense, ExpenseAdmin)
