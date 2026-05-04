from django import forms
from .models import Order, Meal


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['student', 'notes']

    widgets = {
        'notes': forms.Textarea(attrs={'rows': 3}),
    }

