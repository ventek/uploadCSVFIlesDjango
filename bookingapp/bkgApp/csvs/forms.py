from django import forms

from .models import CSVB, CSVI


class CSVModelFormB(forms.ModelForm):
    class Meta:
        model = CSVB
        fields = ('file_name_booking',)


class CSVModelFormI(forms.ModelForm):
    class Meta:
        model = CSVI
        fields = ('file_name_inventory',)

