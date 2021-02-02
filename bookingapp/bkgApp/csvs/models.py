from django.db import models


# Create your models here.
class CSVB(models.Model):
    file_name_booking = models.FileField(upload_to='csvb')
    uploaded = models.DateTimeField(auto_now_add=True)
    # Finish process and change activated to true
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File ID: {self.file_name_booking}'


class CSVI(models.Model):
    file_name_inventory = models.FileField(upload_to='csvi')
    uploaded = models.DateTimeField(auto_now_add=True)
    # Finish process and change activated to true
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File ID: {self.file_name_inventory}'

