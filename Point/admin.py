from django.contrib import admin
from .models import Marker
from leaflet.admin import LeafletGeoAdmin


@admin.register(Marker)
class MarkerAdmin(LeafletGeoAdmin):
    list_display=(
        'name','location')
    list_per_page=2
    fields = ('name','location')


    def save_model(self, request, obj, form, change):
        # Fetch the name field value from the form's cleaned data
        name = form.cleaned_data.get('name')

        obj.save()
    

