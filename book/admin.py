from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class bookingAdmin(SummernoteModelAdmin):
    list_display = ('name', 'reference', 'booking_date', 'status')
    search_fields = ('name', 'reference', 'booking_date', 'status')
    prepopulated_fields = {'slug': ('reference',)}
    list_filter = ('status', 'booking_date', 'author')
    summernote_fields = ('notes')
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(status=1)
