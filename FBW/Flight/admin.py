from django.contrib import admin

from Flight.models import Flight

class AdminFlight(admin.ModelAdmin):
    list_display = ['aeroplane','departure','destination',
                   'arrival_datetime',
                   'max_passengers','price']
    list_filter = ['aeroplane','destination','max_passengers', 'departure']
    readonly_fields = ['total_duration']
    search_fields =['departure']
     

admin.site.register(Flight, AdminFlight)
# Register your models here.
