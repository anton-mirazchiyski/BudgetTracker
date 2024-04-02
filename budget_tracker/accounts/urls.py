from django.urls import path, include

from budget_tracker.accounts.views import AccountCreateView, login_user, logout_user, change_currency, \
    show_profile_details, delete_profile_photo, AccountDeleteView, delete_user_data

app_name = 'accounts'

urlpatterns = [
    path('auth/', include([
        path('account-create/', AccountCreateView.as_view(), name='create-account'),
        path('login/', login_user, name='login-account')
    ])),
    path('logout/', logout_user, name='logout-account'),
    path('<int:pk>/profile/', show_profile_details, name='details-profile'),
    path('<int:pk>/profile/photo-delete/', delete_profile_photo, name='delete-profile-photo'),
    path('<int:pk>/profile/currency/', change_currency, name='change-currency'),
    path('<int:pk>/account-delete/', AccountDeleteView.as_view(), name='delete-account'),
    path('<int:pk>/account-delete/delete/', delete_user_data, name='delete-user-data'),
]
