#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput || echo "Error en collectstatic"
python manage.py makemigrations || echo "Error en makemigrations"
python manage.py migrate || echo "Error en migrate"