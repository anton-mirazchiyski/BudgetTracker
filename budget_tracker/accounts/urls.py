from django.urls import path, include

from budget_tracker.accounts.views import AccountCreateView, login_user

app_name = 'accounts'

urlpatterns = [
    path('auth/', include([
        path('account-create/', AccountCreateView.as_view(), name='create_account'),
        path('login/', login_user, name='login_account')
    ]))
]
