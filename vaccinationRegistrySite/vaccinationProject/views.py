from rest_framework.response import Response
import json
from django.http import HttpResponse
from sqlalchemy import null
from .models import *
from .serializers import *
from rest_framework import generics
from datetime import date
from rest_framework import status, permissions
from rest_framework.reverse import reverse
from django_filters import FilterSet, DateFilter, TimeFilter, BooleanFilter, NumberFilter, CharFilter, ModelChoiceFilter
from django.core.paginator import Paginator


class Index(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    name = 'index'
    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'userDetails': reverse(UserDetailsList.name, request=request),
            'vaccines': reverse(VaccineList.name, request=request),
            'facilities': reverse(FacilityList.name, request=request),
            'visits': reverse(VisitList.name, request=request),
            'free-visit-list': reverse(FreeVisitList.name, request=request),
            'profile': reverse(Profile.name, request=request),
            'admin_panel': "http://127.0.0.1:8000/admin/",
        })
    

class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer
    name = 'users-list'
    # filter_fields = ['role', 'is_active']
    # search_fields = ['username', 'role']
    # ordering_fields = ['username', 'role', 'is_active']
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer
    name = "user-detail"


class UserDetailsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer
    name = "userdetails-list"
    filter_fields = ['country', 'city', 'zip_code','gender', 'is_vaccinated']
    search_fields = ['firstname','lastname','pesel','date_of_birth','country','city','street','zip_code','phone_number','gender','is_vaccinated']
    ordering_fields = ['firstname', 'lastname', 'country', 'city', 'gender','is_vaccinated']
    

class UserDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailVacinatedSerializer
    name = "userdetails-detail"
    
    
class UserDetailsVacinated(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailVacinatedSerializer
    name = "userdetails-vacinated"
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        if(instance.is_vaccinated == True):
            return Response({"detail": "This patient is already vaccinated"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            instance.is_vaccinated = True
            instance.save()

            return Response({"detail": "You have successfully make this patient vaccinated! Good work! Got userDetails do see more", "url": "http://127.0.0.1:8000/userDetails"}, status=status.HTTP_200_OK)



class VaccineList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    name = "vaccines-list"
    filter_fields = ['name', 'manufacturer']
    search_fields = ['name', 'manufacturer', 'expiration_date']
    ordering_fields = ['name', 'manufacturer', 'expiration_date']


class VaccineDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    name = "vaccine-detail"
    

class FacilityList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    name = " facilities-list"
    filter_fields = ['country', 'city']
    search_fields = ['name', 'country', 'city', 'street', 'contact_phone']
    ordering_fields = ['name', 'country', 'city', 'street']


class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    name = "facility-detail"
    

class VisitFilter(FilterSet):
    from_date = DateFilter(field_name = 'visit_date', lookup_expr = "gte")
    to_date = DateFilter(field_name = 'visit_date', lookup_expr="lte")
    from_time = TimeFilter(field_name = 'visit_time', lookup_expr="gte")
    to_time = TimeFilter(field_name='visit_time', lookup_expr="lte")
    took_place = BooleanFilter(field_name='took_place')
    id_patient = ModelChoiceFilter(queryset=AuthUser.objects.all())
    id_facility = ModelChoiceFilter(queryset=Facility.objects.all())
    id_vaccine = ModelChoiceFilter(queryset=Vaccine.objects.all())
    

class VisitList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    name = "visits-list"
    filter_class = VisitFilter
    filter_fields = ['visit_date', "visit_time",'id_patient','id_facility','id_vaccine', 'took_place']
    search_fields = ['visit_date', "visit_time",'id_patient','id_facility','id_vaccine']
    ordering_fields = ['visit_date', "visit_time", 'id_facility', 'id_vaccine', 'took_place']


class VisitDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Visit.objects.all()
    serializer_class = VisitConfirmSerializer
    name = "visit-detail"
    

class VisitConfirm(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Visit.objects.all()
    serializer_class = VisitConfirmSerializer
    name = "visit-confirm"
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        if(instance.id_patient == None):
            return Response({"detail": "This visit hasn't any patient. :) Cannot confirm..."}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            instance.took_place = True
            instance.save()

            return Response({"detail": "You have successfully confirm to this visit. :) Go to visits to see more", "url": "http://127.0.0.1:8000/visits"}, status=status.HTTP_200_OK)

    

class FreeVisitFilter(FilterSet):
    from_date = DateFilter(field_name='visit_date', lookup_expr="gte")
    to_date = DateFilter(field_name='visit_date', lookup_expr="lte")
    from_time = TimeFilter(field_name='visit_time', lookup_expr="gte")
    to_time = TimeFilter(field_name='visit_time', lookup_expr="lte")
    id_facility = ModelChoiceFilter(queryset=Facility.objects.all())
    id_vaccine = ModelChoiceFilter(queryset=Vaccine.objects.all())
    

class FreeVisitList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Visit.objects.filter(id_patient=None)
    serializer_class = FreeVisitSerializer
    name = "free-visits-list"
    filter_class = FreeVisitFilter
    filter_fields = ['visit_date', "visit_time", 'id_facility', 'id_vaccine']
    search_fields = ['visit_date', "visit_time", 'id_facility', 'id_vaccine']
    ordering_fields = ['visit_date', "visit_time", 'id_facility', 'id_vaccine']
    
    
class FreeVisitDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Visit.objects.all()
    serializer_class = FreeVisitSerializerRegister
    name = "free-visit-detail"
    

class FreeVisitRegister(generics.RetrieveAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Visit.objects.all()
    serializer_class = FreeVisitSerializerRegister
    name = "free-visit-register"
    
    def get(self, request, *args, **kwargs):
        czy = False
        for vi in Visit.objects.filter(id_patient=request.user):
            if vi.took_place == False:
                czy = True 
        if UserDetails.objects.filter(user=request.user)[0].is_vaccinated:
            czy = True
        if(czy):
            return Response({"detail": "You have not done visits or you're fully vaccinated."}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            instance = self.get_object()
            instance.id_patient = request.user
            instance.save()

            return Response({"detail": "You have successfully registered to this visit. :) Go to my visits to see more", "url": "http://127.0.0.1:8000/profile/my-visits"}, status=status.HTTP_200_OK)
        
  
class Profile(generics.ListAPIView):
    permission_classes=[permissions.DjangoModelPermissions]
    queryset = UserDetails.objects.all()
    serializer_class = ProfileSerializer
    name = "profile"
    
    def get_queryset(self, username=0):
        user = UserDetails.objects.filter(user=username)
        return user
    
    def list(self, request, *args, **kwargs):
        username = request.user.id
        queryset = self.filter_queryset(self.get_queryset(username))
        if not queryset.exists():
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class MyVisits(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Visit.objects.all()
    serializer_class = MyVisitDetailSerializer
    name = "my-visit"

    def get_queryset(self, pat=0):
        return Visit.objects.filter(id_patient=pat)

    def list(self, request, *args, **kwargs):
        pat = request.user.id
        queryset = self.filter_queryset(self.get_queryset(pat))
        if not queryset.exists():
            return Response({"detail": "Nie masz żadnych wizyt :)"}, status=status.HTTP_200_OK)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class MyVisitsDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Visit.objects.all()
    serializer_class = MyVisitCancelSerializer
    name = "my-visits-detail"
    
    
class MyVisitsCancel(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Visit.objects.all()
    serializer_class = MyVisitCancelSerializer
    name = "my-visits-cancel"
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        if(instance.took_place == False):
            instance.id_patient = None
            instance.save()

            return Response({"detail": "You have successfully cancel this visit. :) Go to my free visits to see more", "url": "http://127.0.0.1:8000/freevisits"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "This visit is done. :)"}, status=status.HTTP_406_NOT_ACCEPTABLE)