
# path: permite crear rutas para las paginas
from django.urls import path

# views: importa las funciones de nuestro archivo views.py
from . import views


# Lista de rutas de nuestra aplicacion
urlpatterns = [

    # Pagina de inicio de la Semana 3
    path('', views.inicio, name='inicio'),

    # Muestra todos los servicios guardados en MySQL
    path('servicios/', views.servicios, name='servicios'),

    # Permite registrar un nuevo servicio
    path('servicios/nuevo/', views.crear_servicio, name='crear_servicio'),

    # Permite editar un servicio mediante su ID
    path('servicios/<int:pk>/editar/', views.editar_servicio, name='editar_servicio'),

    # Permite eliminar un servicio mediante su ID
    path('servicios/<int:pk>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),

]
