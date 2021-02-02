from django.urls import path

from .views import UploadBookingFile, UploadInventoryFile

app_name = 'csvs'

# noinspection SpellCheckingInspection,SpellCheckingInspection
urlpatterns = [
    path('iupload/', UploadInventoryFile.as_view(), name='UploadInventoryFile'),
    path('bupload/', UploadBookingFile.as_view(), name='UploadBookingFile'),

]

