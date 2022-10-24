# TODO настройте здесь urls для заданий get_car и search_car)
from django.urls import path

from cars.views import get_car, search

urlpatterns = [
    path("search/", search),
    path("<int:pk>/", get_car),
]
