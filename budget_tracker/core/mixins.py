from django.views import generic as views

from budget_tracker.core.accounts_utils import get_user_profile
from budget_tracker.core.currencies_utils import get_current_currency
from budget_tracker.core.income_utils import find_highest_income_for_the_month, calc_total_income_for_the_current_month


class IncomeListContextMixin(views.base.ContextMixin):
    def get_context_data(self, **kwargs):
        profile = get_user_profile(self.request)
        context = super().get_context_data(**kwargs)
        context['current_currency'] = get_current_currency(self.request)
        context['highest_income'] = find_highest_income_for_the_month(profile)
        context['total_income'] = calc_total_income_for_the_current_month(profile)
        return context
