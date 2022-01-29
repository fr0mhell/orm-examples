# Пример Django проекта

## Useful packages

* [django-extensions](https://django-extensions.readthedocs.io/en/latest/#:~:text=Django%20Extensions%20is%20a%20collection,admin%20extensions%20and%20much%20more.) - расширенные команды для Django, и много чего еще
* [factory-boy](https://factoryboy.readthedocs.io/en/latest/orms.html#the-djangomodelfactory-subclass) - генерация тестовых данных

## Makefile and shortcuts

В данном проекте используется [Makefile](https://ru.wikipedia.org/wiki/Makefile). Он содержит шорт-каты - 
короткие команды-обертки, внутри которых выполняется 1 и более команда.

Например, для создания нового супер-пользователя для локальной разработки вместо команды

```shell
python3 manage.py createsuperuser --email root@root.ru --username root -v 3
```

можно будет использовать шорткат `createlocalsu`:

```shell
make createlocalsu
```

[Подробнее про Makefile](https://earthly.dev/blog/python-makefile/)

## Docker

Собираем docker-образ проекта:

```shell
docker build . -t orm-examples
```

Создаем контейнер

```shell
docker create --name orm-examples -p 8000:8000 -v "$(pwd)":/home/www/app orm-examples
```

Список всех контейнеров

```shell
docker ps -a
```

Запускаем контейнер

```shell
docker start orm-examples
```

Открываем логи нашего контейнера

```shell
docker logs orm-examples
```

Останавливаем контейнер

```shell
docker stop orm-examples
```

Создаем пустую базу данных

```shell
mkdir db
touch ./db/db.sqlite3
```

Запускаем контейнер

```shell
docker start orm-examples
```

Открываем логи нашего контейнера

```shell
docker logs orm-examples
```

Проваливаемся внутрь контейнера, применяем миграции, создаем суперпользователя и тестовые данные

```shell
docker exec -it orm-examples bash
python3 manage.py migrate
python3 manage.py createsuperuser --email root@root.ru --username root -v 3
python3 manage.py filldb
```

Получаем информацию о контейнере

```shell
docker inspect orm-examples
```

Получаем информацию об IP-адресе

```shell
docker inspect orm-examples | grep -i "ipaddress"
```

Останавливаем и удаляем контейнер

```shell
docker stop orm-examples && docker rm orm-examples
```