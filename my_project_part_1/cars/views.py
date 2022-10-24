from django.http import JsonResponse

from cars.models import Car


def get_car(request, pk):
    if request.method == "GET":
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return JsonResponse({"error": "Does not exist"}, status=404)

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


def search(request):
    if request.method == "GET":
        brand = request.GET.get("brand", None)

        if not brand:
            JsonResponse([], safe=False)

        cars = Car.objects.filter(brand=brand)
        response = []
        for car in cars:
            response.append({
                "id": car.id,
                "name": car.name,
                "brand": car.brand,
                "status": car.status,
            })

        return JsonResponse(response, safe=False)
