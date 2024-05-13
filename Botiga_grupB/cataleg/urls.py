from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),  # View de prova hello
    path('', views.catalegs, name='catalegs'),  # View de tots els catàlegs
    path('<int:id>', views.cataleg, name='cataleg'),  # View que mostra un catàleg (ID per paràmetre)
    path('<int:id>/afegir/', views.afegirProducte, name='afegir'),  # View que permet afegir productes a un catàleg (ID per paràmetre)
    path('<int:id_cataleg>/eliminar/<int:id_prod>', views.eliminarProducte, name='eliminar'),  # View que permet eliminar productes d'un catàleg (ID de catàleg i de producte a eliminar par parámetre)
    path('<int:id_cataleg>/editar/<int:id_prod>', views.editarProducte, name='editar')  # View que permet editar camps d'un producte d'un catàleg (ID de catàleg i de producte a editar per paràmetre)
]