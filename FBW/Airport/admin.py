from django.contrib import admin

from Airport.models import Airport

class AirportAdmin(admin.ModelAdmin):
    

    list_display = ['name','country','code']
    list_filter = ['name','country','code'] 
    search_fields = ['country']


admin.site.register(Airport, AirportAdmin)
# Register your models here.
