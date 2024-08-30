from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=200,name="title")
    price = models.DecimalField(name="price",max_digits=10,decimal_places=2)
    inventory = models.IntegerField(name='inventory')


class Booking(models.Model):
    name = models.CharField(max_length=200,name='name')
    no_of_guest = models.IntegerField(name='no_of_guest')
    booking_date = models.DateField(name='booking_date')