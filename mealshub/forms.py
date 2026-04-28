from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['student', 'date', 'notes']

    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
        'notes': forms.Textarea(attrs={'rows': 3}),
    }
