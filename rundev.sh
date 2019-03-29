#!/usr/bin/env bash
docker build -t wepost:dev -f Dockerfile .
docker run --rm --name wepost-dev -p 8001:8000 wepost:dev ./manage_dev.py runserver