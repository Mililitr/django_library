# Django Library Project

Добро пожаловать в проект Django Library Project! Этот проект представляет собой веб-приложение для управления библиотекой, позволяющее пользователям регистрироваться, входить в систему, брать и возвращать книги, а библиотекарям управлять задолженностями пользователей.

## Установка и запуск

### Предварительные требования

- Python 3.11.1
- Django 5.0.7
- Виртуальное окружение (рекомендуется)

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/django-library.git
   cd django-library
   ```

    Создайте виртуальное окружение и активируйте его:
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
    ```

    Установите зависимости:
    
    ```bash
    pip install -r requirements.txt
    ```

    Примените миграции:
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

    Создайте суперпользователя (для доступа к админке):
    
    ```bash
    python manage.py createsuperuser
    ```

    Запустите сервер разработки:
    
    ```bash
    python manage.py runserver
    ```