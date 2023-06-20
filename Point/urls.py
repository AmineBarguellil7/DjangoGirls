from django.urls import path
from .views import  *


urlpatterns=[
   path('index/',ShowMap, name='ShowMap'),
   path('save_marker/', save_marker, name='save_marker')
]