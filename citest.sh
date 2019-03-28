#!/usr/bin/env bash
docker build -t wepost:test -f Dockerfile.test.df .
docker run --rm --name wepost-test wepost:test  ./runtests.py
