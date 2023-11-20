from django.urls import path

from budget_tracker.common.views import IndexView

app_name = 'common'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]
