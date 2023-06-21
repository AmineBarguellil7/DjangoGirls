from django.shortcuts import render,redirect
from .models import Marker
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.http import JsonResponse
import json

from django.contrib.gis.geos import Point
from django.core import serializers

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import *
from django.urls import reverse_lazy

from django.contrib import messages




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
    if request.user.is_authenticated:
        markers = Marker.objects.all()
        markers_json = serializers.serialize('json', markers)
        return render(request, 'Point/map.html', {'markers': markers_json})
    else:
        return render(request, 'Point/error.html')    



def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("ShowMap")
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('Home')    
    return render(request,'Point/login.html')

def SignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('Home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('Home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('Home')
        
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        #myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
        return redirect('login')
    return render(request, "Point/SignUp.html")    
         

def Home(request):
    return render(request,"Point/Home.html")  


def Logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('Home') 


   


