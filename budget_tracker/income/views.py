from django.shortcuts import render, redirect
from django.views import generic as views

from budget_tracker.core.accounts_utils import get_user_profile
from budget_tracker.core.common_utils import add_to_balance, subtract_from_balance
from budget_tracker.core.currencies_utils import get_current_currency
from budget_tracker.core.income_utils import find_highest_income_for_the_month, calc_total_income_for_the_current_month
from budget_tracker.income.forms import IncomeAddForm
from budget_tracker.income.models import Income


class IncomeListView(views.ListView):
    model = Income
    template_name = 'income/income-list-page.html'

    def get_context_data(self, **kwargs):
        profile = get_user_profile(self.request)
        context = super().get_context_data(**kwargs)
        context['current_currency'] = get_current_currency(self.request)
        context['highest_income'] = find_highest_income_for_the_month(profile)
        context['total_income'] = calc_total_income_for_the_current_month(profile)
        return context

    def get_queryset(self):
        user_profile = get_user_profile(self.request)
        self.queryset = user_profile.income_set.all()
        return super().get_queryset()


def add_income(request):
    current_currency = get_current_currency(request)
    user_profile = get_user_profile(request)

    if request.method == 'POST':
        form = IncomeAddForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.profile = user_profile
            income.currency = current_currency
            income.save()
            add_to_balance(user_profile, income.amount)
            return redirect('income:all-income')
    form = IncomeAddForm()
    return render(request, 'income/income-add-page.html', {
        'form': form, 'current_currency': current_currency
    })


def delete_income(request, pk):
    user_profile = get_user_profile(request)
    income = user_profile.income_set.filter(pk=pk).get()
    subtract_from_balance(user_profile, income.amount)
    income.delete()
    return redirect('income:all-income')
