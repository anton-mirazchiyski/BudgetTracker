from django.urls import path

from budget_tracker.income.views import IncomeListView

app_name = 'income'

urlpatterns = [
    path('all/', IncomeListView.as_view(), name='all-income'),
]
