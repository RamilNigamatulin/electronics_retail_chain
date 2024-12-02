## Описание проекта

Electronics retail chain  — это Backend-часть онлайн платформу-торговой сети электроники.

Он разработан с использованием Django и Django REST Framework. 

## Требования

- Python 3.11
- Django 4.2
- DRF 3.15
- PostgreSQL 10+

## Установка
1. Клонируйте репозиторий: https://github.com/RamilNigamatulin/electronics_retail_chain.git
2. Создайте виртуальное окружение и активируйте его:
    ```
    python -m venv venv
    ```
    ```
    source venv/bin/activate
    ```
3. Переименуйте файл ".env.sample" в ".env" и заполните его.
Для генерации SECRET_KEY введите в консоль команду: 
    ```
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```
4. Установите зависимости командой: 
    ```
    pip install -r requirements.txt
    ```
5. Запустите проект:
    ```
    python manage.py runserver
    ```
6. Для тестирования проекта возможно использования подготовленных фикстур, для их загрузки введите команду:
    ```
    python manage.py loaddata fixtures/general.json
    ```
    или по отдельности: 
    ```
    python manage.py loaddata fixtures/electronics.json
    ```
    ```
    python manage.py loaddata fixtures/user.json
    ```
- Пароль для всех пользователей 123qwe.
7. Для использования чистой базы и настройки администратора, внесите соответствующие изменения в файл "csu.py" (логин и пароль администратора) и введите команду: 
    ```
    python manage.py csu
    ```

## Эндпоинты

- **Авторизация и аутентификация**:
  - Регистрация пользователя
    ```
    POST /users/register/
    ``` 
    ```
    {
      "email": "user@example.ru",
      "password": "example"
    }
    ```
  - Получение токена
    ```
    POST /users/token/
    ``` 
    ```
    {
      "email": "user@example.ru",
      "password": "example"
    }
    ```
  - Обновление токена
    ```
    POST /users/token/refresh/
    ```
    ```
    {
      "email": "user@example.ru",
      "password": "example"
    }
    ```
  
- **Сетевая организация**:
  - CRUD для организации
    ```
    GET /electronics/
    ``` 
  - Создание сетевой организации
    ```
    POST /electronics/create/
    ``` 
    ```
    {
      "name": "Тест Завод",
      "email": "test@example.ru",
      "link_type": "FC"
    }
    ```
  - Детальная информация об организации
    ```
    GET /electronics/<int:id>/
    ```
  - Редактирование организации
    ```
    PUT /electronics/<int:id>/update/
    ```
    ```
    {
      "name": "Тест Завод 1",
      "email": "test@example.ru",
      "link_type": "FC"
      "level": 1
    }
    ```
  - Удаление организации
    ```
    DELETE /electronics/<int:id>/delete/
    ```

- **Продукты**:
  - CRUD для продуктов
    ```
    GET /products/
    ``` 
  - Создание продукта
    ```
    POST /products/create/
    ``` 
    ```
    {
      "title": "Тест техника"
    }
    ```
  - Детальная информация о продукте
    ```
    GET /products/<int:id>/
    ```
  - Редактирование продукта
    ```
    PUT /products/<int:id>/update/
    ```
    ```
    {
      "title": "Тест техника 1"
    }
    ```
  - Удаление продукта
    ```
    DELETE /products/<int:id>/delete/
    ```
     
- **Поиск**:
  - Поиск организаций по стране 
    ```
    GET /electronics?search=example
    ```