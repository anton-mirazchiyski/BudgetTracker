from django.contrib import admin

from budget_tracker.income.models import Income


class IncomeAdmin(admin.ModelAdmin):
    list_display = ['source', 'amount', 'profile']


admin.site.register(Income, IncomeAdmin)
