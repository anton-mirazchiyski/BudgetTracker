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
            'description': forms.Textarea(attrs={'rows': 12, 'cols': 30}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class ExpenseDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
            self.fields[field].widget.attrs['readonly'] = 'readonly'
            if field != 'description':
                self.fields[field].widget.attrs['class'] = 'form-input expense-form-input'
            else:
                self.fields[field].widget.attrs['class'] = 'expense-description-input'

    class Meta:
        model = Expense
        fields = ['description', 'amount', 'date']

        widgets = {
            'description': forms.Textarea(attrs={'rows': 12, 'cols': 30}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class ExpenseDeleteChoiceForm(forms.Form):
    DELETE_WITH_MONEY_RETURN = 'Delete WITH money returning to balance'
    DELETE_WITHOUT_MONEY_RETURN = 'Delete WITHOUT money returning to balance'

    CHOICES = (
        (DELETE_WITH_MONEY_RETURN, DELETE_WITH_MONEY_RETURN),
        (DELETE_WITHOUT_MONEY_RETURN, DELETE_WITHOUT_MONEY_RETURN),
    )

    delete_choice = forms.CharField(
        widget=forms.RadioSelect(choices=CHOICES, attrs={'class': 'radio-select'})
    )
