from django.shortcuts import render
from Point.models import Marker
from django.core import serializers
from .models import Polygone
from django.contrib.gis.geos import Polygon
from django.http import JsonResponse
from django.contrib.gis.db.models.functions import Area


import json

def ShowMap(request):
    if request.user.is_authenticated:
        markers = Marker.objects.all()
        polygons = Polygone.objects.all()
        markers_json = serializers.serialize('json', markers)
        polygons_json = serializers.serialize('json', polygons)
        return render(request, 'Point/map.html', {'markers': markers_json , 'polygons': polygons_json})
    else:
        return render(request, 'Point/error.html')  



def save_polygon(request):
    if request.method == 'POST':
        polygon_data = json.loads(request.body)
        location = polygon_data.get('location')
        if location:
            polygon_coords = []
            for coord in location:
                polygon_coords.append((coord[0], coord[1]))
            polygon_geom = Polygon(polygon_coords)
            polygon_obj = Polygone.objects.create(location=polygon_geom)
            surface_area = polygon_obj.location.area
            return JsonResponse({'status': 'success', 'surface_area': surface_area})
    return JsonResponse({'status': 'error'})
 