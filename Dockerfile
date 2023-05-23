FROM python:3.11

WORKDIR /docker-web-server

COPY . /docker-web-server

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 8080