from django.db import models

# created = models.DateTimeField(auto_now_add=True)
# title = models.CharField(max_length=100, blank=True, null=True, default='')
# category = models.TextField()
# age = models.IntegerField()


class UserDetails(models.Model):
    firstname = models.CharField(max_length=45, blank=False, null=False)
    lastname = models.CharField(max_length=45, blank=False, null=False)
    pesel = models.CharField(max_length=11, blank=False, null=False)
    date_of_birth = models.DateField(default='1500-01-01')
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
        return self.pesel


class User(models.Model):
    id_user_details = models.OneToOneField(
        UserDetails, related_name="user",  on_delete=models.CASCADE)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    role = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username

    
    
class Vaccine(models.Model):
    manufacturer = models.CharField(max_length=55)
    expiration_date=models.DateField()
    name = models.CharField(max_length=45)
    
    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45)
    contact_phone = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name


class Visit(models.Model):
    visit_date = models.DateField(blank=True, default='1000-01-01')
    visit_time = models.TimeField(blank=True, default='00:00:00')
    id_patient = models.ForeignKey(User, related_name='visit', null=True, blank=True, on_delete=models.DO_NOTHING)
    id_facility = models.ForeignKey(Facility, related_name='visit', null=False, blank=False, on_delete=models.DO_NOTHING)
    id_vaccine = models.ForeignKey(Vaccine, related_name='visit', null=False, blank=False, on_delete=models.DO_NOTHING)
    took_place=models.BooleanField(default=0)
    
    def __str__(self):
        return  self.visit_date+self.visit_time
