руководство по деплою сервиса локально

создание виртуального окружения:

```
python -m venv venv
```

активация виртуального окружения
ДЛЯ WINDOWS

```
venv/Scripts/activate
```

ДЛЯ UNIX*

```
source venv/bin/activate
```

установка зависимостей

```
pip install -r requirements.txt
```

запуск

```
python manage.py runserver
```

установка на winserver

https://github.com/Johnnyboycurtis/webproject/
(взять оттуда web.config)
