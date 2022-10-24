# Задание 1. tech support.py

from django.http import JsonResponse
from tech_support.models import Statistic


def statistics(request):
    if request.method == "GET":
        statistic = Statistic.objects.all()
        response = []
        for record in statistic:
            response.append({
                "id": record.id,
                "store": record.store,
                "author": record.author,
                "status": record.status,
                "day": record.day,
                "reason": record.reason,
                "timestamp": record.timestamp,
            })
        return JsonResponse(response, safe=False)
