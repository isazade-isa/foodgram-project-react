import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    """
    Загружаем ингредиенты в базу из csv файла,
    который располагается в директории /data/
    """

    def handle(self, *args, **options):
        self.import_ingredients()
        print('Загрузка ингредиентов завершена.')

    def import_ingredients(self, file='ingredients.csv'):
        print(f'Загрузка {file}...')
        file_path = f'./data/{file}'
        with open(file_path, newline='', encoding='utf-8') as i:
            reader = csv.reader(i)
            for row in reader:
                Ingredient.objects.update_or_create(
                    name=row[0],
                    measurement_unit=row[1]
                )
