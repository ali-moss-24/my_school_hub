from django.shortcuts import render
from .models import Trip
from .forms import BookingForm


def trip_list(request):
    trips = Trip.objects.all()

    return render(
        request,
        'schooltrips/trip_list.html',
        {'trips': trips}
    )


def create_booking(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()

            return render(
                request,
                'schooltrips/booking_success.html'
            )

    else:
        form = BookingForm()

    return render(
        request,
        'schooltrips/booking_form.html',
        {'form': form}
    )