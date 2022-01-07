from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status


@csrf_exempt
@api_view(('GET',))
def index(request):
    return Response("Hello, world. You're at the vaccination page.")


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsList(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer
    

class UserDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer


class VaccineList(generics.ListCreateAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer


class VaccineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    

class FacilityList(generics.ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    

class VisitList(generics.ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    

class FreeVisitList(generics.ListAPIView):
    queryset = Visit.objects.filter(id_patient=None, visit_date__gte=date.today()).order_by('visit_date', 'visit_time')
    serializer_class = VisitSerializer
    

# TODO: show only active user profile    
class Profile(generics.ListAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer
    
    def get_queryset(self):
        return UserDetails.objects.filter(pk=self.kwargs['profile_id'])
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

#TODO: FreeVisitRegister
