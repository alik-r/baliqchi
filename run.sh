#!/bin/bash
cd baliqchi

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
gunicorn --workers 3 baliqchi.wsgi:application --bind 0.0.0.0:8000
