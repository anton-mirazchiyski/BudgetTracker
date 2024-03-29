from django.core.exceptions import ObjectDoesNotExist

from budget_tracker.accounts.models import UserProfile, ProfilePhoto


def get_user_pk(request):
    user_pk = request.user.pk
    return user_pk


def get_user_profile(request):
    user = request.user
    user_profile = UserProfile.objects.filter(user=user).get()
    return user_profile


def get_profile_photo(profile):
    try:
        photo = ProfilePhoto.objects.filter(user_profile=profile).get()
    except ObjectDoesNotExist:
        photo = None
    return photo
