from django import forms

from budget_tracker.income.models import Income


class IncomeAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-input income-form-input'

    class Meta:
        model = Income
        fields = ('source', 'amount', 'type')

        labels = {
            'source': 'Source of Income:',
            'amount': 'Amount:',
            'type': 'Type of Income:',
        }
