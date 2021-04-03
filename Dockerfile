FROM python:3.9.1-slim-buster

### Set ROOT priveleges
ENV C_FORCE_ROOT=True

### Set default workdir inside container
WORKDIR /home/www/app

### Set Django config
ENV DJANGO_SETTINGS_MODULE=config.development

### Add source code to container
COPY . /home/www/app/

### Install dependencies
RUN pip install --no-cache-dir --src=/src -r /home/www/app/requirements/development.txt

### Collect static
RUN python3 manage.py collectstatic --noinput

### Django port 8000 is externally awailable
EXPOSE 8000

### Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
