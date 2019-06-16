from django.shortcuts import render
from django.http import HttpResponse
def welcome(request):
    all_images = Image.objects.all()
    return render(request,'index.html',{'all_images':all_images})
def search_results(request):
    
    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'index.html',{"message":message,"all_images": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'index.html',{"message":message})

