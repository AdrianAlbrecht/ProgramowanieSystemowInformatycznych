from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User as AuthUser
from rest_framework.reverse import reverse
from . import views

class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    apartament_number = serializers.CharField(required=False)
    user = serializers.SlugRelatedField(queryset=AuthUser.objects.all(),slug_field="username")
    class Meta:
        model = UserDetails
        fields = ['url','id' , 'user', 'firstname','lastname','pesel','date_of_birth','country','city','street','house_number','apartament_number','zip_code','phone_number','gender','is_vaccinated']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #id_user_details = serializers.SlugRelatedField(queryset=UserDetails.objects.all(),slug_field="id")
    class Meta:
        model = AuthUser
        fields = ['url','id', 'username','email','first_name','last_name','is_staff'] #'id_user_details'


class VaccineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaccine
        fields = ['url', 'id', 'name', 'manufacturer', 'expiration_date']


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facility
        fields = ['url','id', 'name', 'country', 'city', 'street','contact_phone']


class VisitSerializer(serializers.HyperlinkedModelSerializer):
    id_patient = serializers.SlugRelatedField(queryset=AuthUser.objects.all(),slug_field="id", required=False)
    id_facility = serializers.SlugRelatedField(queryset=Facility.objects.all(),slug_field="id")
    id_vaccine = serializers.SlugRelatedField(queryset=Vaccine.objects.all(),slug_field="id")
    class Meta:
        model = Visit
        fields = ['url','id','visit_date', "visit_time",'id_patient','id_facility','id_vaccine', 'took_place']
        
class FreeVisitSerializer(serializers.HyperlinkedModelSerializer):
    id_patient = serializers.SlugRelatedField(queryset=AuthUser.objects.all(),slug_field="id", required=False)
    id_facility = serializers.SlugRelatedField(queryset=Facility.objects.all(),slug_field="id")
    id_vaccine = serializers.SlugRelatedField(queryset=Vaccine.objects.all(),slug_field="id")
    url = serializers.HyperlinkedIdentityField(view_name='free-visit-detail')
    class Meta:
        model = Visit
        fields = ['url','id','visit_date', "visit_time",'id_patient','id_facility','id_vaccine', 'took_place']
        
class FreeVisitSerializerRegister(serializers.HyperlinkedModelSerializer):
    id_patient = serializers.SlugRelatedField(queryset=AuthUser.objects.all(),slug_field="id", required=False)
    id_facility = serializers.SlugRelatedField(queryset=Facility.objects.all(),slug_field="id")
    id_vaccine = serializers.SlugRelatedField(queryset=Vaccine.objects.all(),slug_field="id")
    url = serializers.HyperlinkedIdentityField(view_name='free-visit-register')
    class Meta:
        model = Visit
        fields = ['url','id','visit_date', "visit_time",'id_patient','id_facility','id_vaccine', 'took_place']
        
        
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    apartament_number = serializers.CharField(required=False)
    user = serializers.SlugRelatedField(queryset=AuthUser.objects.all(),slug_field="username")
    url = serializers.ReadOnlyField(default='http://127.0.0.1:8000/profile/my-visits')
    class Meta:
        model = UserDetails
        fields = ['url','id' , 'user', 'firstname','lastname','pesel','date_of_birth','country','city','street','house_number','apartament_number','zip_code','phone_number','gender','is_vaccinated']


        
class MyVisitDetailSerializer(serializers.HyperlinkedModelSerializer):
    id_patient = serializers.SlugRelatedField(queryset=AuthUser.objects.all(),slug_field="id", required=False)
    id_facility = serializers.SlugRelatedField(queryset=Facility.objects.all(),slug_field="id")
    id_vaccine = serializers.SlugRelatedField(queryset=Vaccine.objects.all(),slug_field="id")
    url = serializers.HyperlinkedIdentityField(view_name='my-visits-detail')
    class Meta:
        model = Visit
        fields = ['url','id','visit_date', "visit_time",'id_patient','id_facility','id_vaccine', 'took_place']
    