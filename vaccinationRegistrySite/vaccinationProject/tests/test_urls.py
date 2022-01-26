from django.test import SimpleTestCase
from django.urls import reverse, resolve
from vaccinationProject.views import UserList
from vaccinationRegistrySite.vaccinationProject import views

class TestUrls(SimpleTestCase):
    def test_UserList_is_resolved(self):
        # assert 1==2
        url=reverse(views.UserList.name)
        print(resolve(url))
        self.assertEquals(resolve(url).func,UserList)

