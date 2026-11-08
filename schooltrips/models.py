from django.db import models


PAYMENT_CHOICES = [
    ('FULL', 'Pay in Full'),
    ('PARTIAL', 'Voluntary Contribution'),
    ('LATER', 'Pay Later')
]


class Trip(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Booking(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    parent_name = models.CharField(max_length=100)
    consent = models.BooleanField(default=False)
    payment_choice = models.CharField(
       max_length=10,
       choices=PAYMENT_CHOICES
    )

    contribution_amount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.parent_name} - {self.trip.name}"