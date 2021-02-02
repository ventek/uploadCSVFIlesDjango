from django.urls import path

from .views import InventoryListView, BookingList, BookingView, index, registerPage, loginPage, logoutUser

app_name = 'booking'

urlpatterns = [
    path('inventory_list/', InventoryListView.as_view(), name='InventoryList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='BookingView'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('', index, name='home'),
]

