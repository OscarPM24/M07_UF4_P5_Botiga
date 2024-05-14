from django.urls import path
from . import views
#Defició de les rutes per accedir a les diferents views de carreto
urlpatterns = [
    path('', views.index, name="index"), #View index
    path('<int:id>', views.carretoActual, name="carretoActual"), #View carretoActual
    path('<int:id>/afegeixProducte', views.afegeixProducte, name='afegeixProducte'), #View afegeixProducte
    path('<int:id>/eliminaProducte/<int:producte_id>', views.eliminaProducte, name='eliminaProducte'), #View eliminaProducte
    path('<int:id>/eliminaCarreto/', views.eliminaCarreto, name="eliminaCarreto"), #View eliminaCarreto
    path('<int:id>/modificaQuantitat/<int:producte_id>', views.modificaQuantitat, name='modificaQuantitat'), #View modificaQuantitat
]