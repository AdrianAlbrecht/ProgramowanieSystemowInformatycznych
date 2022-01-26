from django.contrib import admin

from .models import *

admin.site.register(UserDetails)
admin.site.register(Vaccine)
admin.site.register(Facility)
admin.site.register(Visit)
