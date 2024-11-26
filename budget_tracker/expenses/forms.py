from django import forms

from budget_tracker.expenses.models import Expense


class ExpenseBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-input expense-form-input'

    class Meta:
        model = Expense
        fields = ['description', 'amount', 'date']

        widgets = {
            'description': forms.TextInput(attrs={}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class ExpenseAddForm(ExpenseBaseForm):
    pass


class ExpenseDeleteForm(ExpenseBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
            self.fields[field].widget.attrs['readonly'] = 'readonly'
