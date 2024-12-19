FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY 	. /code/

RUN python manage.py collectstatic --settings=chat_project.settings.local

EXPOSE 8000

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:$PORT"]

