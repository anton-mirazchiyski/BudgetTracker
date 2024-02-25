from django.urls import path

from budget_tracker.expenses.views import ExpenseListView

app_name = 'expenses'

urlpatterns = [
        path('', ExpenseListView.as_view(), name='all-expenses'),
]
