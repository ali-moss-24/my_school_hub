from django import forms
from .models import Order

class OrderForm(forms.Model.Form):
    model = Order
    fields = ['student', 'date', 'notes']

    widgets = {
        'date': forms.DataInput(attrs={'type': 'date'}),
        'notes': forms.Textarea(attrs={'rows': 3}),
    }