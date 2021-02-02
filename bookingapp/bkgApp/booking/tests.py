import datetime

from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from .models import Booking
from .views import BookingView


# Create your tests here.
# noinspection SpellCheckingInspection,SpellCheckingInspection
class BookingTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='John', email='john@doe.com', password='top_secret')

    def test_fields(self):
        item = Booking()
        item.user = self.user
        item.title = 'Bali-Test'
        item.remaining_count = 5
        item.description = "This is a discription with  intended double spaces"
        item.updated = datetime.datetime.now().tzinfo
        item.created = datetime.datetime.now().tzinfo
        item.expiration_date = '2020-02-03'
        item.save()

        record = Booking.objects.get(pk=1)
        self.assertEqual(record, item)

    def test_views(self):
        # Create an instance of a GET request.
        request = self.factory.get('/availibility_form')
        request.user = self.user
        # an AnonymousUser instance.
        request.user = AnonymousUser()
        # Test my_view()
        response = BookingView()
        # Use this syntax for class-based views.
        response = BookingView.as_view()(request)
        self.assertEqual(response.status_code, 200)
