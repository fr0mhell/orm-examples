# IMPORTANT

* [Deleting docker entities](https://phoenixnap.com/kb/remove-docker-images-containers-networks-volumes)


# First version


## Build container

```bash
docker build -t version-01 .
```

## Run container

```bash
docker run -dp 8000:8000 version-01 "python3" "manage.py" "runserver"
```

## Get IP of container

```bash
docker inspect v01 | grep -i "ipaddress"
```

## Get inside the container

```bash
docker exec -it v01 bash
```

## Stop and remove container

```bash
docker stop v01 && docker rm v01
```


# Second version


## Build container

```bash
docker build -t version-02 .
```

## Run container

```bash
docker run --name v02 version-02
```

## Stop and remove container

```bash
docker stop v02 && docker rm v02
```


# Third version


## Build production container

```bash
docker build -t version-03 --build-arg DJANGO_ENV=production .
```

## Run container

```bash
docker run --name v03 version-03
```

## Stop and remove container

```bash
docker stop v03 && docker rm v03
```

## Build development container

```bash
docker build -t version-03 .
```


# Fourth version


## Build development container

```bash
docker build -t version-04 .
```

## Run with a volume

```bash
docker run -dp 8000:8000 --name v04 -v ~/Projects/orm-examples:/home/www/app version-04
```


# Add docker-compose


## Simple backend service

```bash
docker-compose build backend
docker-compose run backend "python" "manage.py" "migrate"
docker-compose up backend
```

## Backend with postgresql

```bash
docker-compose up -d postgres
docker-compose build backend
docker-compose run backend-prod "python" "manage.py" "migrate"
docker-compose up backend-prod
```

### Easy way to reset DB with docker-compose

```bash
docker-compose stop postgres && docker-compose rm -f postgres && docker-compose up -d postgres
```
