# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
from django.urls import path

from courses.views import courses, new_courses, get_course, search

urlpatterns = [
    path("new/", new_courses),
    path("search/", search),
    path("<str:slug>/", get_course),
    path("", courses),
]
