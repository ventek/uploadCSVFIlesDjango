from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Inventory


class AvailabilityForm(forms.Form):
    title = forms.ChoiceField(choices=Inventory.INV_CATAGORIES, required=True)
    trip_from_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
