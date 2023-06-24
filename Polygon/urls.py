from django.urls import path
from .views import  *



urlpatterns = [
   path('index/', ShowMap, name='showMap'),
   path('save_polygon/', save_polygon, name='save_polygon'),
]