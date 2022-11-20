from django.shortcuts import render
from django.views import generic
from .models import Booking

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('booking_date')
    paginate_by = 5
