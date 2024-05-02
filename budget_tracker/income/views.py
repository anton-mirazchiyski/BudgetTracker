from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from budget_tracker.core.accounts_utils import get_user_profile
from budget_tracker.core.common_utils import add_to_balance, subtract_from_balance, get_current_month
from budget_tracker.core.currencies_utils import get_current_currency
from budget_tracker.core.mixins import IncomeListContextMixin
from budget_tracker.income.forms import IncomeAddForm, IncomeUpdateForm
from budget_tracker.income.models import Income


class IncomeListView(IncomeListContextMixin, views.ListView):
    model = Income
    template_name = 'income/income-list-page.html'

    def get_queryset(self):
        user_profile = get_user_profile(self.request)
        self.queryset = user_profile.income_set.all().order_by('date')
        return super().get_queryset()


class IncomeByTypeListView(views.ListView):
    model = Income
    template_name = 'income/income-list-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_currency'] = get_current_currency(self.request)
        return context

    def get_queryset(self):
        user_profile = get_user_profile(self.request)
        income_type = self.kwargs['type']
        self.queryset = user_profile.income_set.filter(type=income_type)
        return self.queryset


class IncomeByCurrentMonthListView(IncomeListContextMixin, views.ListView):
    model = Income
    template_name = 'income/income-list-page.html'

    def get_queryset(self):
        user_profile = get_user_profile(self.request)
        current_month = get_current_month()
        self.queryset = user_profile.income_set.filter(date__month=current_month)
        return self.queryset


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


class IncomeUpdateView(views.UpdateView):
    model = Income
    form_class = IncomeUpdateForm
    template_name = 'income/income-edit-page.html'
    success_url = reverse_lazy('income:all-income')


def delete_income(request, pk):
    user_profile = get_user_profile(request)
    income = user_profile.income_set.filter(pk=pk).get()
    subtract_from_balance(user_profile, income.amount)
    income.delete()
    return redirect('income:all-income')
