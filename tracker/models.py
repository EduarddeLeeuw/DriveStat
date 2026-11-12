from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    model_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100, choices=[('CAR', 'Car'),('MOPED','Moped'),('MOTORCYCLE','Motorcycle'),('TRUCK','Truck'),('BUS','Bus')])
    year = models.IntegerField()
    engine_type = models.CharField(max_length=100, choices=[('GAS','Gas'),('DIESEL','Diesel'),('ELECTRIC','Electric')])

    def __str__(self):
        return self.model_name

class Refuel(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    odo = models.IntegerField()
    quantity = models.FloatField()
    date = models.DateField()
    cost = models.FloatField()

    def __str__(self):
        return str(self.odo)

class Trip(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    odo_start = models.IntegerField()
    odo_end = models.IntegerField()
    duration = models.DurationField()
    datetime_end = models.DateTimeField()

    def __str__(self):
        return str(self.vehicle)