from django.urls import path

from budget_tracker.income.views import IncomeListView, add_income, delete_income, IncomeByTypeListView

app_name = 'income'

urlpatterns = [
    path('all/', IncomeListView.as_view(), name='all-income'),
    path('add/', add_income, name='add-income'),
    path('<str:type>/', IncomeByTypeListView.as_view(), name='earned-income'),
    path('<str:type>/', IncomeByTypeListView.as_view(), name='passive-income'),
    path('<int:pk>/delete', delete_income, name='delete-income'),
]
