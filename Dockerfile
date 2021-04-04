FROM python:3.9.1-slim-buster

### Set ROOT privileges
ENV C_FORCE_ROOT=True

### Set default workdir inside container
WORKDIR /home/www/app

### Django port 8000 is externally available
EXPOSE 8000

### Run Django server
### The command executes when `docker run`, NOT when `docker build`
CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:8000"]

### Install base dependencies
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y \
        nginx \
        supervisor \
        postgresql-client \
        cron && \
    # cleaning up unused files
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false  && \
    rm -rf /var/lib/apt/lists/*

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
