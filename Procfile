web: gunicorn mysite.wsgi
release:    
  - python manage.py migrate
  - python manage.py loaddata your_fixture_file.json