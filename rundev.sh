#!/usr/bin/env bash
docker build -t wepost:dev -f Dockerfile .
docker run --rm --name wepost-dev --mount type=volume,src=wepost-db,target=/opt/data/ -p 8001:8000 wepost:dev ./manage_dev.py runserver 0.0.0.0:8000