

from django.test import TestCase

from vaccinationProject.models import UserDetails, Vaccine


class TestModels(TestCase):
    def setUp(self):
        self.user1=UserDetails.objects.create(
            firstname = 'Karol',
            lastname = 'Wallen',
            pesel = '62091692878',
            date_of_birth = '1500-01-01',
            country = 'Poland',
            city = 'Olsztyn',
            street = 'Kanta',
            house_number = '121',
            apartament_number = '12',
            zip_code = '12-543',
            phone_number = '606505986',
            gender = 'male',
            is_vaccinated = True
        )
        self.vaccine1 = Vaccine.objects.create(
            name='Pfizer',
            manufacturer='PfizerCorporation',
            expiration_date='1999-11-21'
        )
        
    def test_userDetails(self):
        self.assertEquals(self.user1.firstname,'Karol')
    
    def test_vaccine(self):
        self.assertEquals(self.vaccine1.name,'Pfizer')