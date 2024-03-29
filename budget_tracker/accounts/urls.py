from django.urls import path, include

from budget_tracker.accounts.views import AccountCreateView, login_user, logout_user, change_currency, \
    add_profile_photo, ProfileDetailsView

app_name = 'accounts'

urlpatterns = [
    path('auth/', include([
        path('account-create/', AccountCreateView.as_view(), name='create-account'),
        path('login/', login_user, name='login-account')
    ])),
    path('logout/', logout_user, name='logout-account'),
    path('<int:pk>/profile/details/', add_profile_photo, name='add-profile-photo'),
    path('<int:pk>/profile/details/', ProfileDetailsView.as_view(), name='details-profile'),
    path('<int:pk>/profile/currency', change_currency, name='change-currency')
]
