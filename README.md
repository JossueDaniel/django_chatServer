# Django_ChatServer
Este proyecto es una aplicación web que permite que los usuarios se registren y una vez autenticados se les permite unirse a salas de chat en donde podrán comunicarse gracias al protocolo websocket, los usuarios también tienen la opción de crear y eliminar sus propias salas.

## Características
- Protocolo WebSocket para la comunicación en tiempo real.
- Base de datos postgres para alamcenar la infromación de los usuarios y las salas de chat.
- Arquitectura Pub/Sub con redis lo que permite manejar los mensajes en tiempo real entre usuaios conectados al websocket.

## Requisitos previos
- python 3.10 o superior
- docker
- doker-compose

## Estructura del proyecto
```plaintext
django_chatServer/
├── manage.py
├── Dockerfile
├── compose.yml
├── requirements.txt
├── accounts/
├── chat/
├── templates/
└── chat_project/
    └── settings/
        ├── base.py
        ├── local.py
        └── prod.py
```

## Configuración y ejecución
### 1. Clonar repositorio
```bash
git clone https://github.com/JossueDaniel/django_chatServer.git
```

```bash
cd django_chatServer
```

### 2. Establecer las variables de entorno
En el archivo compose.yml establecer la siguiente variable de entorno:

```plainttext
environment:
  - SECRET_KEY=my-custom-secret-key
```

El contendor de la aplicación web se ejecuta en entrono de desarrollo, si se requiere ejecutar en un entorno de producción se debe especificar en la variable de entorno del contenedor en el archivo compose.yml las configuraciones del archivo prod.py que es para entorno de producción. (opcional)
```plaintext
environment:
  - DJANGO_SETTINGS_MODULE=django_project.settings.prod
```
### 3. Construir y levantar los contenedores
```bash
docker compose up --build
```

### 4. Ejecutar las migraciones
```bash
docker compose exec web python manage.py migrate
```

### 5. Crear un superusuario (opcional)
```bash
docker compose exec web createsuperuser
```
### 6. Ingresar a la aplicación
http://localhost:8000/



