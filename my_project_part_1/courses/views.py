from courses.models import Course
from django.http import JsonResponse


def courses(request):
    if request.method == "GET":
        courses_list = Course.objects.all()

        response = []
        for course in courses_list:
            response.append(
                {
                    "id": course.id,
                    "slug": course.slug,
                    "author": course.author,
                    "description": course.description,
                    "start_day": course.start_day,
                    "status": course.status,
                    "created": course.created,
                }
            )
        return JsonResponse(response, safe=False)


def new_courses(request):
    if request.method == "GET":
        courses_list = Course.objects.filter(status="new")

        response = []
        for course in courses_list:
            response.append(
                {
                    "id": course.id,
                    "slug": course.slug,
                    "author": course.author,
                    "description": course.description,
                    "start_day": course.start_day,
                    "status": course.status,
                    "created": course.created,
                }
            )
        return JsonResponse(response, safe=False)


def get_course(request, slug):
    if request.method == "GET":
        try:
            course = Course.objects.get(slug=slug)
        except Course.DoesNotExist:
            return JsonResponse({"error": "Does not exist"}, status=404)

        return JsonResponse({
            "id": course.id,
            "slug": course.slug,
            "author": course.author,
            "description": course.description,
            "start_day": course.start_day,
            "status": course.status,
            "created": course.created,
        })


def search(request):
    if request.method == "GET":
        author = request.GET.get("author", None)
        courses_list = Course.objects.filter(author=author)

        response = []
        for course in courses_list:
            response.append(
                {
                    "id": course.id,
                    "slug": course.slug,
                    "author": course.author,
                    "description": course.description,
                    "start_day": course.start_day,
                    "status": course.status,
                    "created": course.created,
                }
            )
        return JsonResponse(response, safe=False)
