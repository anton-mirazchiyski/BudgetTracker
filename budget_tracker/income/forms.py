from django import forms

from budget_tracker.income.models import Income


class IncomeAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Income
        fields = ('source', 'amount')

        labels = {
            'source': 'Source of Income',
            'amount': 'Amount'
        }
