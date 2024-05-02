from django.urls import path

from budget_tracker.income.views import IncomeListView, add_income, delete_income, IncomeByTypeListView, \
    IncomeByCurrentMonthListView, IncomeUpdateView

app_name = 'income'

urlpatterns = [
    path('all/', IncomeListView.as_view(), name='all-income'),
    path('add/', add_income, name='add-income'),
    path('<int:pk>/delete/', delete_income, name='delete-income'),
    path('<int:pk>/edit/', IncomeUpdateView.as_view(), name='edit-income'),
    path('current-month/', IncomeByCurrentMonthListView.as_view(), name='current-month-income'),
    path('<str:type>/', IncomeByTypeListView.as_view(), name='earned-income'),
    path('<str:type>/', IncomeByTypeListView.as_view(), name='passive-income'),
    path('<str:type>/', IncomeByTypeListView.as_view(), name='portfolio-income'),
]
