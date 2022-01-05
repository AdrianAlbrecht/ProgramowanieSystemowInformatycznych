from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.UserList.as_view(), name='users'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user'),
    path('userDetails', views.UserDetailsList.as_view(), name='userDetails'),
    path('userDetails/<int:pk>', views.UserDetailsDetail.as_view(), name='userDetail'),
    path('vaccines', views.VaccineList.as_view(), name="vaccines"),
    path('vaccines/<int:pk>', views.VaccineDetail.as_view(), name="vaccine"),
    path('facilities', views.FacilityList.as_view(), name="facilities"),
    path('facilities/<int:pk>', views.FacilityDetail.as_view(), name="facility"),
    path('visits', views.VisitList.as_view(), name="visits"),
    path('visits/<int:pk>', views.VisitDetail.as_view(), name="visit"),
]
