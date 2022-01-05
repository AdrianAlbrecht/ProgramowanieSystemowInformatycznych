from django.contrib import admin
from django.urls import path
from .views import  changePassword, sendMail, sendObjectMail, setValue, index
from .views import signing, saltArgument, createUser

urlpatterns = [
    path('', index),
    path('setValue/',setValue),
    path('signing/',signing),
    path('saltArgument/',saltArgument),
    path('createUser/',createUser, name='createUser'),
    path('changePassword/',changePassword, name='changePassword'),
    path('sendMail/',sendMail),
    path('sendObjectMail/',sendObjectMail),
]
