FROM python:3.9-slim-buster

### Set ROOT privileges
ENV C_FORCE_ROOT=True

### Set default workdir inside container
WORKDIR /home/www/app

### Set Django environment with an argument. `development` if nothing passed
ARG DJANGO_ENV=development
ENV DJANGO_SETTINGS_MODULE=config.${DJANGO_ENV}

### Add dependencies info
COPY requirements ./requirements

### Install dependencies
RUN pip install --no-cache-dir --src=/src -r /home/www/app/requirements/${DJANGO_ENV}.txt

### !!! Add source code to container
COPY api_docs ./api_docs
COPY config ./config
COPY emails ./emails
COPY space_rangers ./space_rangers
COPY manage.py ./manage.py

### Run Django
CMD ["python3", "manage.py", "runserver_plus", "0.0.0.0:8000"]

### Collect static
RUN python3 manage.py collectstatic --noinput
