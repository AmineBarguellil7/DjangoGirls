from django.contrib import admin
from .models import Marker
from leaflet.admin import LeafletGeoAdmin
from geopy.geocoders import OpenCage

@admin.register(Marker)
class MarkerAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
    fields = ('location',)
    list_per_page = 2

    def save_model(self, request, obj, form, change):
        location = form.cleaned_data.get('location')
        obj.location = location

        # Reverse geocode the coordinates to get the place name
        geolocator = OpenCage(api_key='a345db1e3bfc4df98694e675f69306fa')
        location_info = geolocator.reverse((location.y, location.x))
        place_name = location_info.address if location_info else ''

        # Set the name field of the marker object
        obj.name = place_name

        obj.save()
