from django.urls import path

from budget_tracker.expenses.views import ExpenseListView, add_expense

app_name = 'expenses'

urlpatterns = [
        path('', ExpenseListView.as_view(), name='all-expenses'),
        path('add/', add_expense, name='add-expense'),
]
