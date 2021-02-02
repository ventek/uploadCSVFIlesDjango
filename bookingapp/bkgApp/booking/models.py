import datetime

from django.contrib.auth.models import *
from django.contrib.auth.models import User

from .functions.inventory_tuple import INV_CATAGORIES


# Create your models here.


class Inventory(models.Model):
    INV_CATAGORIES = INV_CATAGORIES
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=3, choices=INV_CATAGORIES, default="NAN")
    remaining_count = models.PositiveIntegerField(default=0)
    description = models.TextField(default="NAN")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField()

    def __str__(self):
        return f'{self.title}.User: {self.user} has {self.remaining_count} trips that expires at {self.expiration_date}'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=225, default="", editable=False)
    surname = models.CharField(max_length=225, default="", editable=False)
    trip = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True)
    booking_count = models.PositiveIntegerField(default=0)
    date_joined = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.name} has booked {self.booking_count} bookings for {self.trip} and joined at {self.date_joined}'

    def save(self, *args, **kwargs):
        self.booking_count = self.booking_count + 1
        super().save(*args, **kwargs)


