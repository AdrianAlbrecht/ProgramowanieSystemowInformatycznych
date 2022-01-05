from rest_framework import serializers

class UserDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    firstname = serializers.CharField(max_length=45)
    lastname = serializers.CharField(max_length=45)
    pesel = serializers.CharField(max_length=11 )
    date_of_birth = serializers.DateField()
    country = serializers.CharField(max_length=45)
    city = serializers.CharField(max_length=45)
    street = serializers.CharField(max_length=45)
    house_number = serializers.CharField(max_length=5)
    apartament_number = serializers.CharField(max_length=10)
    zip_code = serializers.CharField(max_length=6)
    phone_number = serializers.CharField(max_length=12)
    gender = serializers.CharField(max_length=45)
    is_vaccinated = serializers.BooleanField(default=False)

    def create(self, validated_data):
        """
        Create and return a new `UserDetailSerializer` instance, given the validated data.
        """
        return UserDetailSerializer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `UserDetailSerializer` instance, given the validated data.
        """
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.passworod = validated_data.get('passworod', instance.passworod)
        instance.pesel = validated_data.get('pesel', instance.pesel)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.street = validated_data.get('street', instance.street)
        instance.house_number = validated_data.get('house_number', instance.house_number)
        instance.apartament_number = validated_data.get('apartament_number', instance.apartament_number)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.is_vaccinated = validated_data.get('is_vaccinated', instance.is_vaccinated)
        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    # id_user_details = serializers.OneToOneField(UserDetails, on_delete=serializers.CASCADE)
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(max_length=45)
    role = serializers.CharField(max_length=45)
    email = serializers.EmailField(max_length=45)
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        """
        Create and return a new `UserDetailSerializer` instance, given the validated data.
        """
        return UserSerializer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `UserDetailSerializer` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.role = validated_data.get('role', instance.role)
        instance.email = validated_data.get('email', instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

class VaccineSerializer(serializers.Serializer):
    manufacturer = serializers.IntegerField()
    expiration_date = serializers.DateTimeField()
    name = serializers.CharField(max_length=45)

    def create(self, validated_data):
        """
        Create and return a new `UserDetailSerializer` instance, given the validated data.
        """
        return VaccineSerializer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `UserDetailSerializer` instance, given the validated data.
        """
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.expiration_date = validated_data.get('expiration_date', instance.expiration_date)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class FacilitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=45)
    country = serializers.CharField(max_length=45)
    city = serializers.CharField(max_length=45)
    street = serializers.CharField(max_length=45)
    contact_phone = serializers.CharField(max_length=12)

    def create(self, validated_data):
        """
        Create and return a new `UserDetailSerializer` instance, given the validated data.
        """
        return FacilitySerializer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `UserDetailSerializer` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.street = validated_data.get('street', instance.street)
        instance.contact_phone = validated_data.get('contact_phone', instance.contact_phone)
        instance.save()
        return instance

class VisitSerializer(serializers.Serializer):
    visit_date = serializers.DateTimeField()
    # id_patient = serializers.ForeignKey(User, null=True, blank=True, on_delete=serializers.DO_NOTHING, default="")
    # id_facility = serializers.ForeignKey(Facility, null=False, blank=False, on_delete=serializers.DO_NOTHING)
    # id_vaccine = serializers.ForeignKey(Vaccine, null=False, blank=False, on_delete=serializers.DO_NOTHING)
    took_place = serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new `UserDetailSerializer` instance, given the validated data.
        """
        return VisitSerializer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `UserDetailSerializer` instance, given the validated data.
        """
        instance.visit_date = validated_data.get('visit_date', instance.visit_date)
        instance.took_place = validated_data.get('took_place', instance.took_place)
        instance.save()
        return instance