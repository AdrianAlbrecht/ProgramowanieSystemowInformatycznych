from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name=views.Index.name),
    path('users', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('userDetails', views.UserDetailsList.as_view(), name=views.UserDetailsList.name),
    path('userDetails/<int:pk>', views.UserDetailsDetail.as_view(), name=views.UserDetailsDetail.name),
    path('userDetails/<int:pk>/vaccinated', views.UserDetailsVacinated.as_view(), name=views.UserDetailsVacinated.name),
    path('vaccines', views.VaccineList.as_view(), name=views.VaccineList.name),
    path('vaccines/<int:pk>', views.VaccineDetail.as_view(), name=views.VaccineDetail.name),
    path('facilities', views.FacilityList.as_view(), name=views.FacilityList.name),
    path('facilities/<int:pk>', views.FacilityDetail.as_view(), name=views.FacilityDetail.name),
    path('visits', views.VisitList.as_view(), name=views.VisitList.name),
    path('visits/<int:pk>', views.VisitDetail.as_view(), name=views.VisitDetail.name),
    path('visits/<int:pk>/confirm', views.VisitConfirm.as_view(), name=views.VisitConfirm.name),
    path('freevisits', views.FreeVisitList.as_view(), name=views.FreeVisitList.name),
    path('freevisits/<int:pk>', views.FreeVisitDetail.as_view(), name=views.FreeVisitDetail.name),
    path('freevisits/<int:pk>/register', views.FreeVisitRegister.as_view(), name=views.FreeVisitRegister.name),
    path('profile', views.Profile.as_view(), name=views.Profile.name),
    path('profile/my-visits', views.MyVisits.as_view(), name=views.MyVisits.name),
    path('profile/my-visits/<int:pk>', views.MyVisitsDetail.as_view(), name=views.MyVisitsDetail.name),
    path('profile/my-visits/<int:pk>/cancel', views.MyVisitsCancel.as_view(), name=views.MyVisitsCancel.name),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
