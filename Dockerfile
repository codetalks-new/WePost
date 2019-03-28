FROM python:3.7-alpine3.8
MAINTAINER banxi1988@gmail.com
RUN apk add --no-cache git
RUN git clone -q --depth 1 https://github.com/banxi1988/WePost.git
WORKDIR WePost
RUN pip install -r requirements/dev.txt

