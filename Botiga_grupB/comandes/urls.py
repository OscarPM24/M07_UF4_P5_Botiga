from django.urls import path
from . import views

urlpatterns = [
    path('historic/<int:id>', views.historic, name="historic"),
]