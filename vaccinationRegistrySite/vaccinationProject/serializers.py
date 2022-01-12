from rest_framework import serializers
from .models import *

class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    apartament_number = serializers.CharField(required=False)
    class Meta:
        model = UserDetails
        fields = ['url','id', 'firstname','lastname','pesel','date_of_birth','country','city','street','house_number','apartament_number','zip_code','phone_number','gender','is_vaccinated']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id_user_details = serializers.SlugRelatedField(queryset=UserDetails.objects.all(),slug_field="id")
    class Meta:
        model = User
        fields = ['url','id', 'id_user_details','role','is_active']


class VaccineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaccine
        fields = ['url', 'id', 'name', 'manufacturer', 'expiration_date']


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facility
        fields = ['url','id', 'name', 'country', 'city', 'street','contact_phone']


class VisitSerializer(serializers.HyperlinkedModelSerializer):
    id_patient = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field="id", required=False)
    id_facility = serializers.SlugRelatedField(queryset=Facility.objects.all(),slug_field="id")
    id_vaccine = serializers.SlugRelatedField(queryset=Vaccine.objects.all(),slug_field="id")
    class Meta:
        model = Visit
        fields = ['url','id','visit_date', "visit_time",'id_patient','id_facility','id_vaccine', 'took_place', 'owner']