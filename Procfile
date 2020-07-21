release: python manage.py makemigrations app
release: python manage.py migrate --no-input
web: gunicorn project.wsgi