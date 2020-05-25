#!/bin/sh
set -e

/app/src/manage.py migrate
exec "$@"