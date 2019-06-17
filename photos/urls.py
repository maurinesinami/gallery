from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^location/(\w+)', views.view_by_location,name='view_by_location'),
    url(r'^category/(\w+)', views.view_by_category,name='view_by_category'),
    url(r'^image/(\d+)', views.View_full_image,name='full_image'),
    url(r'^search/', views.search_category, name='search_category'),
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)