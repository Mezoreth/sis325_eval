from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('cuestionario/nuevo', views.crear_cuestionarios.as_view(), name='cuestionario_n'),
    path('cuestionario/listar', views.listar_cuestionarios.as_view(), name='cuestionario_l'),
    url(r'^cuestionario/editar(?P<pk>\d+)/$',views.editar_cuestionarios.as_view(), name='cuestionario_e'),
    url(r'^cuestionario/ver(?P<pk>\d+)/$',views.ver_cuestionarios.as_view(), name='cuestionario_v'),

    path('pregunta/nuevo', views.crear_pregunta.as_view(), name='pregunta_n'),
    path('respuesta/nuevo', views.crear_respuesta.as_view(), name='respuesta_n'),
    path('index', views.index, name='index')
]