from django.urls import re_path, include, reverse_lazy, path

from . import views
from django.contrib.auth import views as auth_views #import this
urlpatterns = [
    re_path('index', views.index, name='index'),
    re_path('dashboard', views.dashboard, name='dashboard'),
    re_path('gestionUsuarios',views.gestionUsuarios, name='gestionUsuarios'),
    re_path('Eliminar',views.Eliminar, name='Eliminar'),
    re_path('Modificar',views.Modificar, name='Modificar'),
    re_path('Añadir',views.Añadir, name='Añadir'),
    re_path('predicción', views.predicción, name='predicción'),
    re_path('pred2', views.pred2, name='pred2'),
    re_path('pred3', views.pred3, name='pred3'),
    re_path('AgregarUsuario',views.AgregarUsuario, name='AgregarUsuario'),
    re_path('EliminaUsuario',views.EliminaUsuario, name='EliminaUsuario'),
    re_path('borraUsuarios',views.borraUsuarios, name='borraUsuarios'),
    re_path('buscaLista',views.buscaLista, name='buscaLista'),
    re_path('buscamod',views.buscamod,name="buscamod"),
    re_path('modificarU',views.modificarU,name="modificarU"),
    re_path('Perfil', views.Perfil, name='Perfil'),
    re_path('Password', views.Password, name='Password'),
    re_path('Listado',views.Listado, name='Listado'),
    re_path('buscador',views.buscador,name='buscador'),

    path('Borrar/<int:Uid>/',views.Borrar, name='Borrar'),
    path('Editar/<int:Uid>/',views.Editar, name='Editar'),
]