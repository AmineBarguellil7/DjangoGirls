from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Polygone

@admin.register(Polygone)
class PolygonModelAdmin(OSMGeoAdmin):
    list_display = ('location',)
    fields = ('location',)
