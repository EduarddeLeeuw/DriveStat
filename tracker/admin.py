from django.contrib import admin
from .models import Vehicle, Refuel, Trip

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('owner','model_name','vehicle_type', 'year', 'engine_type')
    search_fields = ('owner','model_name','vehicle_type', 'year', 'engine_type')
    list_filter = ('owner','model_name','vehicle_type', 'year', 'engine_type')
    list_display_links = ('model_name',)
    fields = ('owner','model_name','vehicle_type', 'year', 'engine_type')

admin.site.register(Vehicle, VehicleAdmin)

class RefuelAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'odo', 'quantity', 'date', 'cost')
    search_fields = ('vehicle', 'odo', 'quantity', 'date', 'cost')
    list_filter = ('vehicle',  'date',)
    list_display_links = ('vehicle',)
    fields = ('vehicle', 'odo', 'quantity', 'date', 'cost')

admin.site.register(Refuel, RefuelAdmin)

class TripAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'odo_start', 'odo_end', 'duration', 'datetime_end')
    search_fields = ('vehicle', 'odo_start', 'odo_end', 'duration', 'datetime_end')
    list_filter = ('vehicle',  'duration',)
    list_display_links = ('vehicle',)
    fields = ('vehicle', 'odo_start', 'odo_end', 'duration', 'datetime_end')

admin.site.register(Trip, TripAdmin)