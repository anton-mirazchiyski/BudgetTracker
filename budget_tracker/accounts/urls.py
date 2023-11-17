from django.urls import path, include

from budget_tracker.accounts.views import AccountCreateView

urlpatterns = [
    path('auth/', include([
        path('account-create/', AccountCreateView.as_view(), name='create_account')
    ]))
]
