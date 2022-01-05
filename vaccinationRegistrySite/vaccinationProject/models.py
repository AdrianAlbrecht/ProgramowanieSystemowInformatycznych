from django.db import models

# created = models.DateTimeField(auto_now_add=True)
# title = models.CharField(max_length=100, blank=True, null=True, default='')
# category = models.TextField()
# age = models.IntegerField()


class UserDetails(models.Model):
    firstname = models.CharField(max_length=45, blank=False, null=False)
    lastname = models.CharField(max_length=45, blank=False, null=False)
    pesel = models.CharField(max_length=11, blank=False, null=False)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45)
    house_number = models.CharField(max_length=5)
    apartament_number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=12)
    gender = models.CharField(max_length=45)
    is_vaccinated = models.BooleanField(default=False)
    
    def __str__(self):
        return "%s" % self.pesel


class User(models.Model):
    id_user_details = models.OneToOneField(
        UserDetails, on_delete=models.CASCADE)
    username = models.CharField(max_length=45,)
    password = models.CharField(max_length=45)
    role = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return "%s" % self.username

    
    
class Vaccine(models.Model):
    manufacturer=models.IntegerField()
    expiration_date=models.DateTimeField()
    name = models.CharField(max_length=45)
    
    def __str__(self):
        return "%s" % self.name


class Facility(models.Model):
    name = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45)
    contact_phone = models.CharField(max_length=12)
    
    def __str__(self):
        return "%s" % self.name


class Visit(models.Model):
    visit_date=models.DateTimeField()
    id_patient = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, default="")
    id_facility = models.ForeignKey(Facility, null=False, blank=False, on_delete=models.DO_NOTHING)
    id_vaccine = models.ForeignKey(Vaccine, null=False, blank=False, on_delete=models.DO_NOTHING)
    took_place=models.BooleanField()
    
    def __str__(self):
        return "%s %s %s" % (self.id_patient, self.id_facility, self.id_vaccine)
