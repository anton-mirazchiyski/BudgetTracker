from budget_tracker.accounts.models import UserProfile


def get_user_pk(request):
    user_pk = request.user.pk
    return user_pk


def get_user_profile(request):
    user = request.user
    user_profile = UserProfile.objects.filter(user=user).get()
    return user_profile
