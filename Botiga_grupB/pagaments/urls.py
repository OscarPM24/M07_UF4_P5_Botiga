from django.urls import path
from . import views

urlpatterns = [
    path('carreto/<int:id_carreto>/', views.pagarCarreto, name='pagar'),
]