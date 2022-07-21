from django.contrib import admin

from Booking.models import Booking



class BookingAdmin(admin.ModelAdmin):
    list_display =[ 'reference_no','passenger_first_name', 'passenger_last_name', 'flight' ,'booking_datetime']
    list_filter = ['flight','booking_datetime']
    search_fields = ['reference_no']
# Register your models here.



admin.site.register(Booking,BookingAdmin)          
     
    
                   
    