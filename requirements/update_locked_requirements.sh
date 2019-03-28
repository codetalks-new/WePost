#!/usr/bin/env bash
pip-compile requirements/common.in -o requirements/common.txt
pip-compile requirements/prod.in -o requirements/prod.txt
pip-compile requirements/dev.in -o requirements/dev.txt
