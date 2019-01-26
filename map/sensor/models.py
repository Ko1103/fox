from django.db import models
#create your models here.

# primary key id is automatically setted.
# Therefore you don't have to write in here.

class Sensor(models.Model):
    sensor_name = models.CharField(max_length=15)
    value = models.FloatField()
    created_at = models.DateTimeField()
    def __str__(self):
        return self.sensor_name

class Reference(models.Model):
    sensor_name = models.CharField(max_length=15)
    value = models.FloatField()
    temp_value = models.FloatField()
    create_at = models.DateTimeField()

    def __str__(self):
        return self.sensor_name