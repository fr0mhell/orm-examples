makemig:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

createlocalsu:
	python3 manage.py createsuperuser --email root@root.ru --username root -v 3

start_db:
	docker-compose up -d db-dev

filldb:
	python3 manage.py filldb