from django.contrib import admin
from .models import Marker
from leaflet.admin import LeafletGeoAdmin


@admin.register(Marker)
class MarkerAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
    fields = ('location',)
    list_per_page = 2
    def save_model(self, request, obj, form, change):
        location = form.cleaned_data.get('location')
        name = form.cleaned_data.get('name')
        print(name)
        print(location)

        obj.location = location
        obj.save()
