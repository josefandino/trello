Trello CloneCrearunAPIqueemulelasfuncionalidadesbásicasdetrello(https://trello.com/). 

A continuación se describen las historias de usuarios y los campos para cada tabla.

Entregables

1. Documentación de API.

2. Repositorio de código.

  Historias de usuario

  1. Cómo usuario quiero registrarme a la plataforma para crear mi primer tablero.

  2. Cómo usuario quiero crear un tablero desde la página principal para gestionar unproyecto.

  3. Cómo usuario quiero ver la lista de mis tableros y distinguir aquellos seleccionadoscomo favoritos.

  4. Como usuario quiero invitar a otros usuarios (registrados y no registrados) comomiembros del tablero para que puedan acceder a ese proyecto.
  Pero no pueden editarlos detalles del mismo, únicamente agregar elementos.

  5. Cómo usuario quiero agregar listas a mi tablero para agregar tareas a cada una.

  6. Cómo usuario quiero ordenar mis listas para tener mejor control de mi proyecto.

  7. Cómo usuario quiero agregar tarjetas a cada lista para poder asignar responsables decada una.

  8. Cómo usuario quiero asignar miembros o responsables de cada tarea para que leslleguen notificaciones.

  9. Cómo usuario quiero agregar comentarios en cada tarea para poder comunicarme conlos miembros o responsables.

  Tablas

  ● Usuarios

  ○ Nombres (Texto)
  ○ Apellidos (Texto)
  ○ Correo (Texto)
  ○ Contraseña (Texto)

  ● Tableros
  ○ Nombre (Texto)
  ○ Descripción (Texto)
  ○ Fecha de creación (Fecha y hora)
  ○ Dueño (Llave foránea)
  ○ Favorito (Muchos a muchos)
  ○ Visibilidad (Texto, selección)
  ○ Miembros (Muchos a muchos)

  ● Listas
    ○ Nombre (Texto)
    ○ Tablero (Llave foránea)
    ○ Fecha de creación (Fecha y hora)
    ○ Posición (Entero)

  Tarjetas
    ○ Nombre (Texto)
    ○ Lista (Llave foránea)
    ○ Descripción (texto)
    ○ Miembros (Muchos a muchos)
    ○ Dueño (Llave foránea)
    ○ Fecha de creación (Fecha y hora)
    ○ Fecha de vencimiento (Fecha y hora)
    ○ Posición (Entero)

  ● Comentarios
    ○ Tarjeta (Llave foránea)
    ○ Mensaje (Texto)
    ○ Dueño (Llave foránea)
    ○ Fecha de creación (Fecha y hora)



  Consideraciones generales

    ● Envío de correos para notificaciones* 
    ● Base de datos Postgres.*
    ● Pruebas unitarias.
    ● Generar documentación.
    ● Endpoints y actions


# configuracion:
  ● En la carpeta project se debe crear un archivo db.py
  ● importamos estas librerias: os y pathlib

    import os

    from pathlib import Path

        BASE_DIR = Path(__file__).resolve().parent.parent
      db = {
          'default': {
              'ENGINE': 'django.db.backends.sqlite3',
              'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
          }
      }

  ● DATABASES = db

# Para conectar con DB Postgres
## ● En la carpeta project se debe crear un archivo db.py
db = {
   'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'trelloapp',
      'USER': 'postgres',
      'PASSWORD': '123',
      'HOST': 'localhost',
      'PORT': '5432',
    }
}

### en el archivo settings se modifica, quedando de la siguiente manera
● DATABASES = db


