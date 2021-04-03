FROM python:3.9.1-slim-buster

### Set ROOT priveleges
ENV C_FORCE_ROOT=True

### Set default workdir inside container
WORKDIR /home/www/app

### Install base dependencies
RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y nginx  supervisor postgresql-client cron
### Cleaning up unused files
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
RUN rm -rf /var/lib/apt/lists/*

### Set Django environment with an argument. `development` if nothing passed
ARG DJANGO_ENV=development
ENV DJANGO_SETTINGS_MODULE=config.${DJANGO_ENV}

### Add dependencies info
COPY requirements /home/www/app/requirements

### Install dependencies
RUN pip install --no-cache-dir --src=/src -r /home/www/app/requirements/${DJANGO_ENV}.txt

### Add source code to container
COPY . /home/www/app/

### Collect static
RUN python3 manage.py collectstatic --noinput

### Django port 8000 is externally awailable
EXPOSE 8000

### Run Django server
CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:8000"]
