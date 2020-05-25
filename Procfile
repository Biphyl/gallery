release: python manage.py makemigrations
release: python manage.py migrate


web: gunicorn mygallery.wsgi --log-file