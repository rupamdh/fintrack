from django import forms
from .models import *

class SpendingForm(forms.ModelForm):
    class Meta:
        model = Spending
        fields = ('budget', 'amount', 'note')
        
        widgets = {
            # 'budget': forms.Select(choices=Budget.objects.all().values_list('id', 'name')),
            'amount': forms.NumberInput(attrs={'step': '1'}),
            'note': forms.Textarea(attrs={'rows': 2}),
        }

        
class BudgetAddForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'
        exclude = ('user', )