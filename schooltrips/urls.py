from django.urls import path
from . import views

urlpatterns = [
    path('', views.trip_list, name='trip_list'),
    path('book/', views.create_booking, name='create_booking'),

    path(
        'payment-success/',
        views.payment_success,
        name='payment_success'
    ),

    path(
        'payment-cancel/',
        views.payment_cancel,
        name='payment_cancel'
    ),
]