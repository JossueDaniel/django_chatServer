# Extra base python oficial
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establece directorio de trabajo
WORKDIR /code

# Instalación de dependencias
RUN pip install --upgrade pip
COPY  requirements.txt /code/
RUN pip install -r requirements.txt

# Copia el proyecto de Django
COPY . /code/
