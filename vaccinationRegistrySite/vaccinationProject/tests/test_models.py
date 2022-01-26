

from django.test import TestCase

from vaccinationRegistrySite.vaccinationProject.models import Facility, UserDetails, Vaccine, Visit


class TestModels(TestCase):
    def setUp(self):
        self.user1=UserDetails.object.create(
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
            is_vaccinated = True,
        ),
        self.vaccine1 = Vaccine.objects.create(
            name='Pfizer',
            manufacturer='PfizerCorporation',
            expiration_date='1999-11-21'
        ),
        self.facility1 = Facility.objects.create(
            name = 'Placówka Warszawka',
            country = 'Poland',
            city = 'Warszawa',
            street = 'Gdańska',
            contact_phone = '504560982',
        ),
        self.visit1 = Visit.objects.create(
            visit_date = '2022-01-01',
            visit_time = '11:10:00',
            id_patient = 1,
            id_facility = 1,
            id_vaccine = 1,
            took_place=0
        )
    def test_userDetails(self):
        self.assertEquals(self.user1.firstname,'Karol')
    
    def test_vaccine(self):
        self.assertEquals(self.vaccine1.name,'Pfizer')
    
    def test_facitity(self):
        self.assertEquals(self.vaccine1.name,'Placówka Warszawka')
    
    def test_visit(self):
        self.assertEquals(self.visit1.visit_date,'2022-01-01')