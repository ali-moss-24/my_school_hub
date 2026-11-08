from django import forms
from . models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'trip',
            'parent_name',
            'consent',
            'payment_choice',
            'contribution_amount',
        ]