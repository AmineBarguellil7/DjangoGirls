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



import pyproj

def calculate_polygon_area(vertices):
    lats, lons = zip(*vertices)
    lats = list(lats)
    lons = list(lons)
    lats.reverse()  
    lons.reverse()  
    area = pyproj.Geod(ellps='WGS84').polygon_area_perimeter(lats, lons)
    print(area)
    return area[0]





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
            print(polygon_coords)
            surface_area = calculate_polygon_area(polygon_coords) 
            print('Surface Area:', surface_area)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
 