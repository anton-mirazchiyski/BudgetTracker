from django.urls import path

from budget_tracker.common.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]
