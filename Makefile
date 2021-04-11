build:
	docker-compose build backend celery-worker

db:
	docker-compose up -d postgres redis

migrate:
	docker-compose run backend python manage.py migrate

static:
	docker-compose run backend python manage.py collectstatic --noinput

createsu:
	docker-compose run backend python manage.py createsuperuser

nginx:
	docker-compose up -d backend celery-worker nginx
