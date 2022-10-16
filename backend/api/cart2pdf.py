from django.db.models import F, Sum
from django.http import HttpResponse
from django.template.loader import render_to_string

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from recipes.models import IngredientRecipe
from weasyprint import HTML


@action(
    detail=False, methods=['get'], permission_classes=(IsAuthenticated,)
)
def download_shopping_cart(self, request):
    shopping_list = IngredientRecipe.objects.filter(
        recipe__cart__user=request.user
    ).values(
        name=F('ingredient__name'),
        measurement_unit=F('ingredient__measurement_unit')
    ).annotate(amount=Sum('amount')).values_list(
        'ingredient__name', 'amount', 'ingredient__measurement_unit'
    )
    html_template = render_to_string('recipes/pdf_template.html',
                                     {'ingredients': shopping_list})
    html = HTML(string=html_template)
    result = html.write_pdf()
    response = HttpResponse(result, content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=shopping_list.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    return response
