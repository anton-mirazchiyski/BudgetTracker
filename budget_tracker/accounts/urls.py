from django.urls import path, include

from budget_tracker.accounts.views import AccountCreateView, UserLoginView

app_name = 'accounts'

urlpatterns = [
    path('auth/', include([
        path('account-create/', AccountCreateView.as_view(), name='create_account'),
        path('login/', UserLoginView.as_view(), name='login_account')
    ]))
]
