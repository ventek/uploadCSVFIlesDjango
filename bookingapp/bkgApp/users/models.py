from booking.models import Booking
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

