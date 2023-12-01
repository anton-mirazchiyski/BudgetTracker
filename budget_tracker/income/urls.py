from django.urls import path

from budget_tracker.income.views import IncomeListView, IncomeAddView

app_name = 'income'

urlpatterns = [
    path('all/', IncomeListView.as_view(), name='all-income'),
    path('add/', IncomeAddView.as_view(), name='add-income'),
]
