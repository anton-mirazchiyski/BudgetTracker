from django.urls import path

from budget_tracker.common.views import IndexView, show_balance, show_dashboard

app_name = 'common'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('balance/', show_balance, name='balance'),
]
