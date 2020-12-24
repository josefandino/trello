from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API TRELLO",
        default_version='v1',
        description="\n" +
                    "Crear un API que emule las funcionalidades básicas de trello (Trello es un software de " +
                    "administración de proyectos con interfaz web y con cliente para iOS y android para organizar " +
                    "proyectos). A continuación se describen las historias de usuarios y los campos para cada tabla. \n \n" +

                    "Historias de usuario\n" +

                    "\n\t1. Cómo usuario quiero registrarme a la plataforma para crear mi primer tablero." +
                    "\n\t2. Cómo usuario quiero crear un tablero desde la página principal para gestionar un" +
                    "proyecto." +
                    "\n\t3. Cómo usuario quiero ver la lista de mis tableros y distinguir aquellos seleccionados" +
                    "como favoritos." +
                    "\n\t4. Como usuario quiero invitar a otros usuarios (registrados y no registrados) como" +
                    "miembros del tablero \n\tpara que puedan acceder a ese proyecto. Pero no pueden editar" +
                    "los detalles del mismo, únicamente agregar elementos." +
                    "\n\t5. Cómo usuario quiero agregar listas a mi tablero para agregar tareas a cada una." +
                    "\n\t6. Cómo usuario quiero ordenar mis listas para tener mejor control de mi proyecto." +
                    "\n\t7. Cómo usuario quiero agregar tarjetas a cada lista para poder asignar responsables de" +
                    "cada una." +
                    "\n\t8. Cómo usuario quiero asignar miembros o responsables de cada tarea para que les" +
                    "lleguen notificaciones." +
                    "\n\t9. Cómo usuario quiero agregar comentarios en cada tarea para poder comunicarme con" +
                    "los miembros o responsables.",

        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="131108@unamba.edu.pe"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('boards/', include('apps.boards.urls')),
    path('cards/', include('apps.cards.urls')),
    path('comments/', include('apps.comments.urls')),
    path('list/', include('apps.list.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
#
