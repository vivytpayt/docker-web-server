FROM python:3.11

WORKDIR /docker-web-server

COPY . /docker-web-server

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt


RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

EXPOSE 8080

CMD [ "python3", "app.py" ]