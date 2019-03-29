FROM python:3.7-alpine3.8
MAINTAINER banxi1988@gmail.com
ENV PYTHONUNBUFFERED 1
WORKDIR /opt
COPY requirements/dev.txt  /opt/dev.txt
RUN pip install -r dev.txt
EXPOSE 8000
COPY . /opt
