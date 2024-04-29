from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.carretoActual, name="carretoActual"),
    path('<int:id>/afegeixProducte', views.afegeixProducte, name='afegeixProducte'),
    path('<int:id>/eliminaProducte/<int:producte_id>', views.eliminaProducte, name='eliminaProducte'),
    path('<int:id>/eliminaCarreto/', views.eliminaCarreto, name="eliminaCarreto"),
    path('<int:id>/modificaQuantitat/<int:producte_id>', views.modificaQuantitat, name='modificaQuantitat'),
]