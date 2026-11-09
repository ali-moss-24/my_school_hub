from django import forms
from . models import Booking


class BookingForm(forms.ModelForm):

    consent = forms.BooleanField(
        label="I give permission for my child to attend this school trip and confirm that the information provided is accurate."
    )
    
    class Meta:
        model = Booking
        fields = [
            'trip',
            'parent_name',
            'medical_notes',
            'consent',
            'payment_choice',
            'contribution_amount',
        ]