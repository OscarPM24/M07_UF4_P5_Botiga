from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('', views.catalegs, name='catalegs'),
    path('<int:id>', views.cataleg, name='cataleg'),
]