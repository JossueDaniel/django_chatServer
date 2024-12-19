FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/

COPY requirements.txt /code/

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY 	. /code/