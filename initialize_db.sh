#!/usr/bin/env bash

python3.8 /source/config/manage.py collectstatic --noinput -c
python3.8 /source/config/manage.py migrate
python3.8 /source/config/manage.py create_superuser_with_password --noinput --username victor --email victor.augustobarros@gmail.com --password vb@pg
#python3.8 /source/config/manage.py create_user --username victor --email victor.augustobarros@gmail.com --password vb@pg
python3.8 /source/config/manage.py runserver 0.0.0.0:7000
