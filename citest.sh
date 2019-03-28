#!/usr/bin/env bash
docker build -t wepost-test . && docker run --rm -it wepost-test git pull && python runtests.py
