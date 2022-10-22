![workflow](https://github.com/isazade-isa/foodgram-project-react/actions/workflows/final.yml/badge.svg)

## Описание проекта

# Foodgram - «Продуктовый помощник»

Это онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Проект использует базу данных PostgreSQL. Проект запускается в трёх контейнерах (nginx, PostgreSQL и Django) (контейнер frontend используется лишь для подготовки файлов) через docker-compose на сервере. Образ с проектом загружается на Docker Hub.

## Запуск проекта с помощью Docker

1. Склонируйте репозиторий.

   ```
   git clone git@github.com:isazade-isa/foodgram-project-react.git
   ```

2. Создайте .env файл в директории backend/foodgram/ , в котором должны содержаться следующие переменные для подключения к базе PostgreSQL:

   ```
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=postgres
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   DB_HOST=db
   DB_PORT=5432
   ```

3. Перейдите в директорию infra/ и выполните команду для создания и запуска контейнеров.

   ```
   sudo docker compose up -d --build
   ```

4. Войдите в контейнер backend и внутри выполните миграции, создайте суперпользователя, соберите статику и загрузите в бд ингредиенты.

   ```
   sudo docker exec -it <container_ID> bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py collectstatic --no-input
   python manage.py load_ingredients
   ```
