from django.contrib import admin
from .models import Sensor
from .models import Reference

admin.site.register(Sensor)
admin.site.register(Reference)