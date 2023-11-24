web: gunicorn mysite.wsgi
release: 
  - python manage.py migrate
  - python manage.py loaddata --exclude contenttypes data/*.json