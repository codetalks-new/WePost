#!/usr/bin/env bash
docker build -t wepost:dev -f Dockerfile.dev.df .
docker run --rm --name wepost-dev -p 8000:8000 wepost:dev ./manage_dev.py runserver 0.0.0.0:8000
