from django.db.models import Sum
from django.http import HttpResponse

from recipes.models import IngredientRecipe


def download_shopping_cart(self, request):
    ingredients = IngredientRecipe.objects.filter(
        recipe__shopping_cart__user=request.user
    ).values(
        'ingredient__name', 'ingredient__measurement_unit'
    ).order_by(
        'ingredient__name'
    ).annotate(
        ingredient_sum=Sum('amount')
    )
    filename = 'shopping_list.txt'
    shopping_cart = {}
    for item in ingredients:
        name = item.get('ingredient__name')
        count = str(item.get('ingredient_sum')) + ' ' + item.get(
            'ingredient__measurement_unit'
        )
        shopping_cart[name] = count
        data = 'Список покупок:\n\n'
        for num, i in shopping_cart.items():
            data += f'{num} - {i}\n'
    response = HttpResponse(
        data, content_type='text.txt; charset=utf-8'
    )
    response['Content-Disposition'] = (
        f'attachment; filename={filename}.txt'
    )
    return response
