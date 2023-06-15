from django.shortcuts import render
from .models import *  

def ListPost(request):
    Posts=Post.objects.all()
    return render(request, 'Blog/affiche.html',{'p':Posts})

# def index(request):
#     return render(request, 'Blog/index.html')
