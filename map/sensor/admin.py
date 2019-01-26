from django.contrib import admin
from .models import Sensor
from .models import Reference

# Register your models here.

admin.site.register(Sensor)
admin.site.register(Reference)