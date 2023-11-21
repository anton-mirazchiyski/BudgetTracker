from django.urls import path, include

from budget_tracker.accounts.views import AccountCreateView, login_user, logout_user, details_profile

app_name = 'accounts'

urlpatterns = [
    path('auth/', include([
        path('account-create/', AccountCreateView.as_view(), name='create-account'),
        path('login/', login_user, name='login-account')
    ])),
    path('logout/', logout_user, name='logout-account'),
    path('<int:pk>/profile/details', details_profile, name='details profile')
]
