# path: función para definir una ruta individual
from django.urls import path
# views: el archivo que acabás de escribir, en la misma carpeta
from . import views

# urlpatterns: lista de rutas que esta app entiende
urlpatterns = [
    # '': la URL vacía (la raíz de esta app) · views.inicio: la función que la atiende
    # name='inicio': un alias interno para referirse a esta ruta sin escribir la URL a mano
    path('', views.inicio, name='inicio'),
        # nueva ruta 'servicios/' → función views.servicios → alias 'servicios'
    path('servicios/', views.servicios, name='servicios'),
]