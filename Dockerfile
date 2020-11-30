FROM python:3.8

LABEL maintainer="victor.augustobarros@gmail.com"

WORKDIR /source

ADD config /source/config/

COPY initialize_db.sh /source

RUN chmod +x initialize_db.sh

COPY requirements.txt /source

RUN pip install pip --upgrade

RUN pip install --no-cache-dir -r requirements.txt
