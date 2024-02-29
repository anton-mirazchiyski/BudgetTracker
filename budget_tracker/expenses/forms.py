from django import forms

from budget_tracker.expenses.models import Expense


class ExpenseAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'description':
                self.fields[field].widget.attrs['class'] = 'form-input expense-form-input'
            else:
                self.fields[field].widget.attrs['class'] = 'expense-description-input'

    class Meta:
        model = Expense
        fields = ['description', 'amount', 'date']

        widgets = {
            'description': forms.Textarea(attrs={'rows': 10, 'cols': 40}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }
