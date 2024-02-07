from django.shortcuts import render, redirect
from django.views import generic as views

from budget_tracker.core.accounts_utils import get_user_profile
from budget_tracker.core.currencies_utils import get_current_currency
from budget_tracker.income.forms import IncomeAddForm
from budget_tracker.income.models import Income


class IncomeListView(views.ListView):
    model = Income
    template_name = 'income/income-list-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_currency'] = get_current_currency(self.request)
        return context

    def get_queryset(self):
        user_profile = get_user_profile(self.request)
        self.queryset = user_profile.income_set.all()
        return super().get_queryset()


def add_income(request):
    current_currency = get_current_currency(request)
    if request.method == 'POST':
        form = IncomeAddForm(request.POST)
        if form.is_valid():
            user_profile = get_user_profile(request)
            source_of_income = request.POST['source']
            amount_of_income = request.POST['amount']
            user_profile.income_set.create(source=source_of_income, amount=amount_of_income, currency=current_currency)
            return redirect('income:all-income')
    form = IncomeAddForm()
    return render(request, 'income/income-add-page.html', {
        'form': form, 'current_currency': current_currency
    })
