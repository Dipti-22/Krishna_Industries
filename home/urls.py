from django.contrib import admin
from django.urls import path
from home import views                    # from our application import the views

urlpatterns = [
    path('', views.index, name= "home"),   # if some with the blank url reaches send that to views.index and name it as home
    path('about', views.about, name = "about"), # we can addon on such more pages to our applications 
    
    path('services1', views.services1, name = "Daily Use Umbrellas"),
    path('services2', views.services2, name = "Garden umbrellas"),
    path('services3', views.services3, name = "Resort umbrellas"),
    path('contact', views.contact, name= "contact"),
    path('search', views.search, name= "search"),
 
]
