import csv
import random
from datetime import datetime

from booking.models import Inventory, Booking
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View

from .forms import CSVModelFormB, CSVModelFormI
from .functions.processing import title_name
from .models import CSVB, CSVI


# noinspection SpellCheckingInspection
class UploadBookingFile(View):
    form_class = CSVModelFormB
    success_url = reverse_lazy('booking:BookingList')
    template_name = 'uploadbooking.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Reset the upload
            form = CSVModelFormB
            object = CSVB.objects.get(activated=False)
            with open(object.file_name_booking.path, 'r') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')

                for index, row in enumerate(reader):
                    num = '{:04}'.format(random.randrange(1, 10 ** 4))
                    if index == 0:
                        pass
                    else:
                        member_name = row[0]
                        member_surname = row[1]
                        booking_count = row[2]
                        date_joined = row[3]
                        user = User.objects.create(username=row[0] + str(num), email='None', password=row[1],
                                                   first_name=row[0], last_name=row[1], is_staff=0)
                        Booking.objects.create(
                            user=user,
                            name=member_name,
                            surname=member_surname,
                            booking_count=int(booking_count),
                            date_joined=date_joined,
                        )

                object.activated = True
                object.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})


# noinspection SpellCheckingInspection
class UploadInventoryFile(View):
    form_class = CSVModelFormI
    success_url = reverse_lazy('booking:InventoryList')
    template_name = 'uploadinventory.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Reset the upload
            inventory = CSVModelFormI
            object = CSVI.objects.get(activated=False)
            with open(object.file_name_inventory.path, 'r') as f:
                reader = csv.reader(f, delimiter=',', quotechar='"')
                for index, row in enumerate(reader):
                    if index == 0:
                        pass
                    else:

                        title = title_name(row[0])
                        description = row[1]
                        remaining_count = row[2]
                        expiration_date = datetime.strptime(row[3], '%d/%m/%Y').strftime('%Y-%m-%d')
                        Inventory.objects.create(
                            title=title,
                            description=description,
                            remaining_count=remaining_count,
                            expiration_date=expiration_date,
                        )

                object.activated = True
                object.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})

