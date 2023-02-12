from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, this is my first sample Django app")