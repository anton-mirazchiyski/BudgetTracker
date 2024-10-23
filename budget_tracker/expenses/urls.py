from django.urls import path

from budget_tracker.expenses.views import ExpenseListView, add_expense, show_expense_delete_confirmation_and_choices

app_name = 'expenses'

urlpatterns = [
        path('', ExpenseListView.as_view(), name='all-expenses'),
        path('add/', add_expense, name='add-expense'),
        path('delete/<int:pk>/', show_expense_delete_confirmation_and_choices, name='delete-expense'),
]
