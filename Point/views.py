from django.shortcuts import render
from .models import Marker

from django.http import JsonResponse
import json

from django.contrib.gis.geos import Point
from django.core import serializers


def save_marker(request):
    if request.method == 'POST':
        marker_data = json.loads(request.body)
        location = marker_data.get('location')
        print(location)
        print(marker_data.get('name'))
        if location:
            # Extract latitude and longitude from the location field
            lng, lat = location[6:-1].split()
            # Save the marker data to the database
            marker = Marker.objects.create(name=marker_data.get('name'), location=Point(float(lng), float(lat)))
            # Return a JSON response indicating success
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})



def ShowMap(request):
    markers = Marker.objects.all()
    markers_json = serializers.serialize('json', markers)
    return render(request, 'Point/map.html', {'markers': markers_json})


