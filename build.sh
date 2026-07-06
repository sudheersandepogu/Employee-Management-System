#!/usr/bin/env bash
set -e
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py shell -c "from django.contrib.auth import get_user_model; import os; User = get_user_model(); username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin'); email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com'); password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Admin123!'); User.objects.filter(username=username).exists() or User.objects.create_superuser(username, email, password)"
python manage.py collectstatic --noinput
