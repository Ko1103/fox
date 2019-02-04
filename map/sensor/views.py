import django_filters
from rest_framework import viewsets, filters
from .models import Sensor, Reference
from .serializer import SensorSerializer, ReferenceSerializer

class SensorViewset(viewsets.ModelViewSet):
    queryset = Sensor.objects.all() # modelはデフォルトでobjectsを持つ
    serializer_class = SensorSerializer

class ReferenceViewset(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer