from django.urls import path
from .views import  *



urlpatterns = [
   path('index/', ShowMap, name='ShowMap'),
   path('save_marker/', save_marker, name='save_marker'),
   path('home/',Home,name='Home'),
   path('signUp/',SignUp, name='SignUp'),
   path('login/', Login, name='login'),
   path('logout/', Logout, name='logout'),
]