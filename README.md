# Описание проекта:
> API сервис реализующий функцию социальной сети Yatube, где пользователи могут создавать, удалять и редактировать свои посты, оставлять комментарии под публикациями и подсписываться на других авторов.

# Как запустить проект:

> Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

```
cd kittygram
```

> Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

> Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

> Выполнить миграции:

```
python3 manage.py migrate
```

> Запустить проект:

```
python3 manage.py runserver
```
# Примеры запросов к API:
> GET: /api/v1/posts/

> POST: /api/v1/posts/

> GET: /api/v1/posts/{post_id}/comments/

> POST: /api/v1/follow/

> По адресу /redoc доступна полная документация в формате Redoc для API Yatube 
