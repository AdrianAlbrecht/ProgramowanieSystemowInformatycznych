from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from datetime import date
from rest_framework import status
from rest_framework.reverse import reverse
from django_filters import FilterSet, DateFilter, TimeFilter, BooleanFilter, NumberFilter, CharFilter, ModelChoiceFilter


class Index(generics.GenericAPIView):
    name = 'index'
    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'userDetails': reverse(UserDetailsList.name, request=request),
            'vaccines': reverse(VaccineList.name, request=request),
            'facilities': reverse(FacilityList.name, request=request),
            'visits': reverse(VisitList.name, request=request),
            'free-visit-list': reverse(FreeVisitList.name, request=request),
        })
    

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'users-list'
    filter_fields = ['role', 'is_active']
    search_fields = ['username', 'role']
    ordering_fields = ['username', 'role', 'is_active']
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "user-detail"


class UserDetailsList(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer
    name = "userdetails-list"
    filter_fields = ['country', 'city', 'zip_code','gender', 'is_vaccinated']
    search_fields = ['firstname','lastname','pesel','date_of_birth','country','city','street','zip_code','phone_number','gender','is_vaccinated']
    ordering_fields = ['firstname', 'lastname', 'country', 'city', 'gender','is_vaccinated']
    

class UserDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer
    name = "userdetails-detail"


class VaccineList(generics.ListCreateAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    name = "vaccines-list"
    filter_fields = ['name', 'manufacturer']
    search_fields = ['name', 'manufacturer', 'expiration_date']
    ordering_fields = ['name', 'manufacturer', 'expiration_date']


class VaccineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    name = "vaccine-detail"
    

class FacilityList(generics.ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    name = " facilities-list"
    filter_fields = ['country', 'city']
    search_fields = ['name', 'country', 'city', 'street', 'contact_phone']
    ordering_fields = ['name', 'country', 'city', 'street']


class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    name = "facility-detail"
    

class VisitFilter(FilterSet):
    from_date = DateFilter(field_name = 'visit_date', lookup_expr = "gte")
    to_date = DateFilter(field_name = 'visit_date', lookup_expr="lte")
    from_time = TimeFilter(field_name = 'visit_time', lookup_expr="gte")
    to_time = TimeFilter(field_name='visit_time', lookup_expr="lte")
    took_place = BooleanFilter(field_name='took_place')
    id_patient = ModelChoiceFilter(queryset = User.objects.all())
    id_facility = ModelChoiceFilter(queryset=Facility.objects.all())
    id_vaccine = ModelChoiceFilter(queryset=Vaccine.objects.all())
    

class VisitList(generics.ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    name = "visits-list"
    filter_class = VisitFilter
    filter_fields = ['visit_date', "visit_time",'id_patient','id_facility','id_vaccine', 'took_place']
    search_fields = ['visit_date', "visit_time",'id_patient','id_facility','id_vaccine']
    ordering_fields = ['visit_date', "visit_time", 'id_facility', 'id_vaccine', 'took_place']


class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    name = "visit-detail"
    

class FreeVisitList(generics.ListAPIView):
    queryset = Visit.objects.filter(id_patient=None)
    serializer_class = VisitSerializer
    name = "free-visits-list"
    filter_fields = ['visit_date', "visit_time", 'id_facility', 'id_vaccine']
    search_fields = ['visit_date', "visit_time", 'id_facility', 'id_vaccine']
    ordering_fields = ['visit_date', "visit_time", 'id_facility', 'id_vaccine']
    

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
