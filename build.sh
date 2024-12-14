#!/bin/bash

# Build the project
echo "Installing dependencies..."
python3.10 -m pip install -r requirements.txt

echo "Making Migrations..."
python3.10 manage.py makemigrations --noinput
python3.10 manage.py migrate --noinput

echo "Collecting Static Files..."
python3.10 manage.py collectstatic --noinput --clear
