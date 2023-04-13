lint:
	flake8 manage.py | flake8 hexlet_django_blog

start:
	python manage.py runserver 0.0.0.0:8080