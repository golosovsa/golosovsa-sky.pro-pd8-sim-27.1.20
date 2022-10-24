# Задание 1. tech support.py

from django.http import JsonResponse
from tech_support.models import Statistic


def statistics(request):
    return JsonResponse(Statistic.)
