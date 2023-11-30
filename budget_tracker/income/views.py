from django.shortcuts import render
from django.views import generic as views

from budget_tracker.accounts.models import UserProfile
from budget_tracker.income.models import Income


def get_user_pk(request):
    user_pk = request.user.pk
    return user_pk


def get_user_profile(request):
    user = request.user
    user_profile = UserProfile.objects.filter(user=user).get()
    return user_profile


class IncomeListView(views.ListView):
    model = Income
    template_name = 'income/income-list-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_pk'] = get_user_pk(self.request)
        return context

    def get_queryset(self):
        user_profile = get_user_profile(self.request)
        self.queryset = user_profile.income_set.all()
        return super().get_queryset()
