from django.contrib import admin

from .models import Inventory, Booking

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Booking)
