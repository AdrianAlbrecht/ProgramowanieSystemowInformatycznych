from django.shortcuts import render
from django.http import HttpResponse

from .serializers import FacilitySerializer


def index(request):
    return HttpResponse("Hello, world. You're at the vaccination page.")
