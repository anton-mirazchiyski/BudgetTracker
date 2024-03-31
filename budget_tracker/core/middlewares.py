from budget_tracker.core.accounts_utils import get_user_profile, get_profile_photo


class ProfilePhotoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_view(self, request, view_func, view_args, view_kwargs):
        profile = get_user_profile(request)
        photo = get_profile_photo(profile)
        if request.user.is_authenticated and photo is not None:
            request.context_variable = photo

    def __call__(self, request):
        response = self.get_response(request)

        return response
