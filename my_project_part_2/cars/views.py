from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from cars.models import Car
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404


# TODO ниже представлена функция, которую необходимо переписать на CBV 'CarView'

@method_decorator(csrf_exempt, name='dispatch')
class CarView(View):
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)

        return JsonResponse({
            "id": car.id,
            "slug": car.slug,
            "name": car.name,
            "brand": car.brand,
            "address": car.address,
            "description": car.description,
            "status": car.status,
            "created": car.created,
        })
