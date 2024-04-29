from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.carretoActual, name="carretoActual"),
    path('<int:id>/afegeixProducte', views.afegeixProducte, name='afegeixProducte'),
    path('<int:id>/eliminaProducte/<int:producte_id>', views.eliminaProducte, name='eliminaProducte'),
]