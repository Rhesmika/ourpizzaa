from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class bookingAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('reference',)}
    list_filter = ('status', 'booking_date', 'author')
    summernote_fields = ('notes')
