руководство по деплою сервиса

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
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
```
