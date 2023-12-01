from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from budget_tracker.core.accounts_utils import get_user_profile
from budget_tracker.core.currencies_utils import get_current_currency
from budget_tracker.income.forms import IncomeForm
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


class IncomeAddView(views.CreateView):
    model = Income
    template_name = 'income/income-add-page.html'
    form_class = IncomeForm
    success_url = reverse_lazy('income:all-income')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_currency'] = get_current_currency(self.request)
        return context

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.queryset.add(self.object)
        return HttpResponseRedirect(super().get_success_url())
