from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name=views.Index.name),
    path('users', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('userDetails', views.UserDetailsList.as_view(), name=views.UserDetailsList.name),
    path('userDetails/<int:pk>', views.UserDetailsDetail.as_view(), name=views.UserDetailsDetail.name),
    path('vaccines', views.VaccineList.as_view(), name=views.VaccineList.name),
    path('vaccines/<int:pk>', views.VaccineDetail.as_view(), name=views.VaccineDetail.name),
    path('facilities', views.FacilityList.as_view(), name=views.FacilityList.name),
    path('facilities/<int:pk>', views.FacilityDetail.as_view(), name=views.FacilityDetail.name),
    path('visits', views.VisitList.as_view(), name=views.VisitList.name),
    path('visits/<int:pk>', views.VisitDetail.as_view(), name=views.VisitDetail.name),
    path('freevisits', views.FreeVisitList.as_view(), name=views.FreeVisitList.name),
    path('profile<int:profile_id>', views.Profile.as_view(), name=views.Profile.name),
]
