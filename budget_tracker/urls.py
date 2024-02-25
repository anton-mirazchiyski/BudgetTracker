"""
URL configuration for budget_tracker project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('budget_tracker.common.urls')),
    path('users/', include('budget_tracker.accounts.urls')),
    path('income/', include('budget_tracker.income.urls')),
    path('expenses/', include('budget_tracker.expenses.urls')),
]
