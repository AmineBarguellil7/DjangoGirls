from django.urls import path
from .views import  *


urlpatterns=[
   path('index/', ListPost, name='ListPost'),
   path('post/<int:pk>/', post_detail, name='post_detail'),
   path('post/new/', post_new, name='post_new'),
]