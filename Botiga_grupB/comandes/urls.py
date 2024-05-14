from django.urls import path
from . import views

#Defició de les rutes per accedir a les diferents views de comandes
urlpatterns = [
    path('historic/<int:id>', views.historic, name="historic"), #View historic
    path('pendents', views.pendents, name='pendents'), #View pendents
]