makemig:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

createlocalsu:
	python3 manage.py createsuperuser --email root@root.ru --username root -v 3

start-dev:
	docker-compose up -d db-dev redis

filldb:
	python3 manage.py filldb

makemig-prod:
	docker-compose exec -it backend-prod python manage.py makemigrations

migrate-prod:
	docker-compose exec -it backend-prod python manage.py migrate

createlocalsu-prod:
	docker-compose exec -it backend-prod python manage.py createsuperuser --email root@root.ru --username root -v 3

filldb-prod:
	docker-compose exec -it backend-prod python manage.py filldb

start-prod:
	docker-compose up -d backend-prod db-prod nginx redis

collectstatic:
	python manage.py collectstatic