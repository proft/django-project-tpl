from django.shortcuts import render_to_response
from django.conf import settings


def error404(request):
    return render_to_response("404.html", {"STATIC_URL": settings.STATIC_URL})


def error500(request):
    return render_to_response("500.html", {"STATIC_URL": settings.STATIC_URL})

