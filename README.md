💻 [Yatube](https://github.com/D-Nevskiy/hw05_final) - полноценная социальная сеть: с авторизацией, персональными лентами, комментариями и возможностью для пользователей подписываться друг на друга.

📁 Для проектирования API использован **Django REST framework**. Документация к API доступна после запуска dev-сервера по адресу: http://127.0.0.1:8000/redoc/


### Примеры запросов
- Получить список всех публикаций. При указании параметров limit и offset выдача работает с пагинацией.

Request:
```GET /api/v1/posts/```

Response:
```{
    "count": 2,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=3",
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2",
    "results": [
        {
            "id": 1,
            "author": "string",
            "text": "string",
            "pub_date": "2023-01-06T11:11:18.273956Z",
            "image": "string",
            "group": 0
        },
        {
            "id": 2,
            "author": "string",
            "text": "string",
            "pub_date": "2023-01-06T11:11:18.273956Z",
            "image": "string",
            "group": 0
        }
    ]
}
```
- Подписка на автора.

Request:
```GET /api/v1/follow/```

Request body:
```
{
    "following": "string"
}
```
Response:
```
{
    "user": "string",
    "following": "string"
}
```

## Порядок установки и запуска приложения на localhost

- Установка и активация виртуальное окружение
```
# Windows:
python -m venv venv
source venv/Scripts/activate 
# MacOS или Linux:
python3 -m venv venv
source venv/bin/activate 
```
- Установка зависимостей из файла requirements.txt
```
pip install -r requirements.txt
```
- Создание и выполнение миграций
```
cd yatube_api
python manage.py makemigrations
python manage.py migrate
```
- Запуск сервера
```
python manage.py runserver
```
- Создание суперпользователя
```
python manage.py createsuperuser
```