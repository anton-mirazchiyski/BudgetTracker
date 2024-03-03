from django.urls import path

from budget_tracker.common.views import index, show_balance

app_name = 'common'

urlpatterns = [
    path('', index, name='home'),
    path('balance/', show_balance, name='balance'),
]
