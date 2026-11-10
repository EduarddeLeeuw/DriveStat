from django.db import models

# Create your models here.
class Vehicle(models.Model):
    model_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100, choices=[('CAR', 'Car'),('MOPED','Moped'),('MOTORCYCLE','Motorcycle'),('TRUCK','Truck'),('BUS','Bus')])
    year = models.IntegerField()
    engine_type = models.CharField(max_length=100, choices=[('GAS','Gas'),('DIESEL','Diesel'),('ELECTRIC','Electric')])

    def __str__(self):
        return self.model_name