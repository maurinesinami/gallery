from django.conf.urls import url
from . import views
urlpatterns=[
    url('^$',views.welcome,name = 'home-page'),
    url(r'^search/', views.search_results, name='search_results')
]