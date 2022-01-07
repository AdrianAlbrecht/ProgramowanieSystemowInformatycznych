from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from datetime import date
from rest_framework import status
from rest_framework.reverse import reverse


class Index(generics.GenericAPIView):
    name = 'index'
    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'userDetails': reverse(UserDetailsList.name, request=request),
            'vaccines': reverse(VaccineList.name, request=request),
            'facilities': reverse(FacilityList.name, request=request),
            'visits': reverse(VisitList.name, request=request),
        })
    

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'users-list'
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "user-detail"


class UserDetailsList(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer
    name = "userdetails-list"
    

class UserDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer
    name = "userdetails-detail"


class VaccineList(generics.ListCreateAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    name = "vaccines-list"


class VaccineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    name = "vaccine-detail"
    

class FacilityList(generics.ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    name = " facilities-list"


class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    name = "facility-detail"
    

class VisitList(generics.ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    name = "visits-list"


class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    name = "visit-detail"
    

class FreeVisitList(generics.ListAPIView):
    queryset = Visit.objects.filter(id_patient=None, visit_date__gte=date.today()).order_by('visit_date', 'visit_time')
    serializer_class = VisitSerializer
    name = "free-visits-list"
    

# TODO: show only active user profile    
class Profile(generics.ListAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer
    name = "profile"
    
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
    

#TODO: FreeVisitRegister with get_object(self)
