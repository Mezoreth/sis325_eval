from django.urls import path

from . import views

urlpatterns = [
    path('cuestionario/nuevo', views.nuevo_cuestionario, name='cuestionario_n'),
    path('cuestionario/pregunta', views.nueva_pregunta, name='pregunta_n'),
    path('index', views.index, name='index')
]