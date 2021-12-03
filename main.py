from vaccinationRegistrySite.vaccinationProject.serializers import FacilitySerializer


def test_FacilitySerializer():
    val_dict = {'name': 'test_name', 'country':'test_country','city': 'test_city', 'street':'test_street','contact_phone': '123123123'}
    serializer = FacilitySerializer(data=val_dict)
    if serializer.is_valid():
        print(serializer.data)
        return serializer.data # assertion test here....
    return serializer.errors

test_FacilitySerializer()