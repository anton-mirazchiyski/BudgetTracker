from django.urls import path

from budget_tracker.common.views import index

app_name = 'common'

urlpatterns = [
    path('', index, name='home'),
]
