from django.urls import path

from budget_tracker.common.views import IndexView, show_balance

app_name = 'common'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('balance/', show_balance, name='balance'),
]
