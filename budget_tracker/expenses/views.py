from django.shortcuts import render, redirect
from django.views import generic as views

from budget_tracker.core.accounts_utils import get_user_profile
from budget_tracker.core.currencies_utils import get_current_currency
from budget_tracker.expenses.forms import ExpenseAddForm
from budget_tracker.expenses.models import Expense


class ExpenseListView(views.ListView):
    model = Expense
    template_name = 'expenses/expense-list-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_currency'] = get_current_currency(self.request)
        return context

    def get_queryset(self):
        user_profile = get_user_profile(self.request)
        self.queryset = user_profile.expense_set.all()
        return super().get_queryset()


def add_expense(request):
    current_currency = get_current_currency(request)

    if request.method == 'POST':
        form = ExpenseAddForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            profile = get_user_profile(request)
            expense.currency = current_currency
            expense.profile = profile
            expense.save()
            return redirect('expenses:all-expenses')
    form = ExpenseAddForm()

    return render(request,
                  'expenses/expense-add-page.html',
                  {'form': form, 'current_currency': current_currency})
