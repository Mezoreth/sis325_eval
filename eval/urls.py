from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('cuestionario/crear', views.CrearCuestionario.as_view(), name='crear_cuestionario'),
    path('cuestionario/listar', views.ListarCuestionarios.as_view(), name='listar_cuestionarios'),
    path('cuestionario/editar/<int:pk>', views.EditarCuestionario.as_view(), name='editar_cuestionario'),
    path('cuestionario/ver/<int:pk>', views.DetalleCuestionario.as_view(), name='detalle_cuestionario'),
    path('cuestionario/eliminar/<int:pk>', views.EliminarCuestionario.as_view(), name='eliminar_cuestionario'),

    path('cuestionario/ver/añadir/<int:pk>', views.AñadirPreguntaCuestionario.as_view(), name='añadir_pregunta_cuestionario'),
    path('cuestionario/ver/añadir/<int:cuestpk>/<int:pregpk>', views.crear_pregunta_cuestionario, name='crear_pregunta_cuestionario'),

    path('materia/crear', views.CrearMateria.as_view(), name='crear_materia'),
    path('materia/listar', views.ListarMaterias.as_view(), name='listar_materias'),
    path('materia/editar/<int:pk>', views.EditarMateria.as_view(), name='editar_materia'),
    path('materia/eliminar/<int:pk>', views.EliminarMateria.as_view(), name='eliminar_materia'),


    path('pregunta/crear', views.CrearPregunta.as_view(), name='crear_pregunta'),

    path('pregunta/crear/fv', views.CrearPreguntaFV.as_view(), name='crear_pregunta_fv'),
    path('pregunta/crear/mru', views.CrearPreguntaMRU.as_view(), name="crear_pregunta_mru"),
    path('pregunta/crear/mrm', views.CrearPreguntaMRM.as_view(), name="crear_pregunta_mrm"),


    path('pregunta/listar', views.ListarPreguntas.as_view(), name='listar_preguntas'),
    path('pregunta/editar/<int:pk>', views.EditarPregunta.as_view(), name='editar_pregunta'),
    path('pregunta/detalle/<int:pk>', views.DetallePregunta.as_view(), name= 'detalle_pregunta'),
    path('pregunta/eliminar/<int:pk>', views.EliminarPregunta.as_view(), name='eliminar_pregunta'),

    path('index', views.index, name='index'),
    path('pregunta/tipo', views.pregunta_tipo, name='tipo_pregunta')
]