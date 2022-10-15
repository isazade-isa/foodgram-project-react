## Описание проекта

# Foodgram - «Продуктовый помощник»

Это онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Проект использует базу данных PostgreSQL. Проект запускается в трёх контейнерах (nginx, PostgreSQL и Django) (контейнер frontend используется лишь для подготовки файлов) через docker-compose на сервере. Образ с проектом загружается на Docker Hub.

## Запуск проекта с помощью Docker

1. Склонируйте репозиторий на локальную машину.

   ```
   git clone git@github.com:isazade-isa/foodgram-project-react.git
   ```

2. Создайте .env файл в директории backend/foodgram/, в котором должны содержаться следующие переменные для подключения к базе PostgreSQL:

   ```
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=postgres
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   DB_HOST=db
   DB_PORT=5432
   ```

3. Перейдите в директорию infra/ и выполните команду для создания и запуска контейнеров.
   `sudo docker compose up -d --build`
   > Возможна команда **$ sudo docker-compose up -d --build** (зависит от версии docker compose)

> В Windows команда выполняется без **sudo**

4. В контейнере backend выполните миграции, создайте суперпользователя и соберите статику.

   ```
   sudo docker compose exec backend python manage.py migrate
   sudo docker compose exec backend python manage.py createsuperuser
   sudo docker compose exec backend python manage.py collectstatic --no-input
   ```

5. Загрузите в бд ингредиенты командой ниже.

   ```
   sudo docker compose exec backend python manage.py load_ingredients
   ```
