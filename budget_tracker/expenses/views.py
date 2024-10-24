from django.shortcuts import render, redirect
from django.views import generic as views

from budget_tracker.core.accounts_utils import get_user_profile
from budget_tracker.core.common_utils import subtract_from_balance
from budget_tracker.core.currencies_utils import get_current_currency
from budget_tracker.core.expenses_utils import delete_expense
from budget_tracker.expenses.forms import ExpenseAddForm, ExpenseDeleteChoiceForm, ExpenseDeleteForm
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
        self.queryset = user_profile.expense_set.all().order_by('date')
        return super().get_queryset()


def add_expense(request):
    current_currency = get_current_currency(request)
    profile = get_user_profile(request)

    if request.method == 'POST':
        form = ExpenseAddForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.currency = current_currency
            expense.profile = profile
            expense.save()
            subtract_from_balance(profile, expense.amount)
            return redirect('expenses:all-expenses')
    form = ExpenseAddForm()

    return render(request,
                  'expenses/expense-add-page.html',
                  {'form': form, 'current_currency': current_currency})


def show_expense_delete_confirmation_and_choices(request, pk):
    profile = get_user_profile(request)
    expense = profile.expense_set.filter().get(pk=pk)

    if request.method == 'POST':
        choice_form = ExpenseDeleteChoiceForm(request.POST)
        if choice_form.is_valid():
            delete_choice = choice_form.cleaned_data.get('delete_choice')
            delete_expense(profile, expense, delete_choice)
            return redirect('expenses:all-expenses')

    form = ExpenseDeleteForm(instance=expense)
    choice_form = ExpenseDeleteChoiceForm()

    context = {
        'form': form,
        'choice_form': choice_form,
        'expense': expense,
    }
    return render(request, 'expenses/expense-delete-page.html', context)

