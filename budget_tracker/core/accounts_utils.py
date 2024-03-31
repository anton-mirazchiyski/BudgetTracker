from django.core.exceptions import ObjectDoesNotExist

from budget_tracker.accounts.models import UserProfile, ProfilePhoto


def get_user_profile(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.filter(user=user).get()
    except TypeError:
        user_profile = None
    return user_profile


def get_profile_photo(profile):
    try:
        photo = ProfilePhoto.objects.filter(user_profile=profile).get()
    except ObjectDoesNotExist:
        photo = None
    return photo
