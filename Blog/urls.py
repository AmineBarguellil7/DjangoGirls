from django.urls import path
from .views import  *


urlpatterns=[
    path("List/",ListPost),
    path("index/",index),
]