from django.contrib import admin
from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('model_name','vehicle_type', 'year', 'engine_type')
    search_fields = ('model_name','vehicle_type', 'year', 'engine_type')
    list_filter = ('model_name','vehicle_type', 'year', 'engine_type')
    list_display_links = ('model_name',)
    fields = ('model_name','vehicle_type', 'year', 'engine_type')

admin.site.register(Vehicle, VehicleAdmin)
