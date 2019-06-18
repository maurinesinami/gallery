from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Image,Location,Category


def home(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html',{"images":images,"locations":locations,"categories":categories})

def view_by_location(request,location_name):
      
    images = Image.get_with_location(location_name)
     #View function for the navbar
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html',{"images":images,"locations":locations,"categories":categories})  

def view_by_category(request,category_name):

    images = Image.get_with_category(category_name)
    #View function for the navbar
    locations = Location.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html',{'images':images,"locations":locations,"categories":categories})

def View_full_image(request,id):
    image = Image.objects.filter(id=id)
    #View function for the navbar
    locations = Location.objects.all()
    categories = Category.objects.all()

    return render(request,'image.html',{'image':image,"locations":locations,"categories":categories})

def search_category(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get("image")
        images =  Image.search_by_category(search_term)
        message = f"{search_term}"
    
        return render(request,'searched.html',{'images':images,"locations":locations,"categories":categories})
    else:
        message = "You haven't searched for any term"
        return render(request,'searched.html',{"locations":locations,"categories":categories})
