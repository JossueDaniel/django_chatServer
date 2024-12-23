FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY 	. /code/

RUN mkdir -p /code/staticfiles

RUN python manage.py collectstatic --settings=chat_project.settings.prod

EXPOSE 8000

CMD ["gunicorn", "chat_project.wsgi:application", "--bind", "0.0.0.0:8000", "--env", "DJANGO_SETTINGS_MODULE=chat_project.settings.prod"]


