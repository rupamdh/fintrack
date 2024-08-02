from django import forms
from .models import *

class SpendingForm(forms.ModelForm):
    class Meta:
        model = Spending
        fields = ('budget', 'amount', 'note')
        
        widgets = {
            # 'budget': forms.Select(choices=Budget.objects.all().values_list('id', 'name')),
            'amount': forms.NumberInput(attrs={'step': '1', 'placeholder': '0', 'autofocus':''}),
            'note': forms.TextInput(attrs={'placeholder': 'Espense Note'}),
        }

        
class BudgetAddForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'
        exclude = ('user', )