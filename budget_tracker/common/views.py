from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views import generic as views


def index(request):
    try:
        current_user_profile = request.user
        profile_pk = current_user_profile.pk
    except ObjectDoesNotExist:
        current_user_profile, profile_pk = None, None

    return render(
        request,
        'common/home-page.html',
        {'profile_pk': profile_pk}
    )
