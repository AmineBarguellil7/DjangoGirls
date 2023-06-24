from django.shortcuts import render
from Point.models import Marker
from django.core import serializers
from .models import Polygone
from django.contrib.gis.geos import Polygon
from django.http import JsonResponse


import json

def ShowMap(request):
    if request.user.is_authenticated:
        markers = Marker.objects.all()
        markers_json = serializers.serialize('json', markers)
        return render(request, 'Point/map.html', {'markers': markers_json})
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
            #surface = polygon_obj.location.transform(srid, clone=False).area
            #surface_meters = polygon_obj.location.transform(27700, clone=False).area
            # print(surface)
            # print(surface_meters)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
 