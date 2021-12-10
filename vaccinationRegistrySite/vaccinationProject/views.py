from django.shortcuts import render
from django.http import HttpResponse

from vaccinationRegistrySite.vaccinationProject.serializers import FacilitySerializer


def index(request):
    val_dict = {'name': 'test_name', 'country': 'test_country', 'city': 'test_city', 'street': 'test_street',
                'contact_phone': '123123123'}
    serializer = FacilitySerializer(data=val_dict)
    if serializer.is_valid():
        print(serializer.data)
        return serializer.data  # assertion test here....
    return serializer.errors
    # return HttpResponse("Hello, world. You're at the vaccination page.")
