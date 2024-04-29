from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('', views.catalegs, name='catalegs'),
    path('<int:id>', views.cataleg, name='cataleg'),
    path('<int:id>/afegir/', views.afegirProducte, name='afegir'),
    path('<int:id_cataleg>/eliminar/<int:id_prod>', views.eliminarProducte, name='eliminar'),
    path('<int:id_cataleg>/editar/<int:id_prod>', views.editarProducte, name='editar')
]