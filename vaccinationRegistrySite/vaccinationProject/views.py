from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the vaccination page.")

@csrf_exempt
def UserList(request):
    
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)
    
@csrf_exempt
def UserDetailsList(request):
    
    if request.method == "GET":
        userDetails = UserDetails.objects.all()
        serializer = UserDetailSerializer(userDetails, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)
    

    