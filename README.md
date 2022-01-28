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


