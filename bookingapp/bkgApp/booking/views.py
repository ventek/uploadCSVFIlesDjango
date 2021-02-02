from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, FormView

from .forms import AvailabilityForm, CreateUserForm
from .functions.availability import trip_availability
from .models import Inventory, Booking


# Create your views here.
# view the trips without using admin
class InventoryListView(ListView):
    model = Inventory


class BookingList(ListView):
    model = Booking


class BookingView(FormView):
    form_class = AvailabilityForm
    # noinspection SpellCheckingInspection
    template_name = 'availibility_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        trip_data = Inventory.objects.filter(title=data['title'])
        print(trip_data)

        for trip in trip_data:
            field_name1 = 'booking_count'
            obj_b = Booking.objects.filter().first()
            booking_count = getattr(obj_b, field_name1)
            if trip_availability(trip, data['title'], booking_count) is True:
                booking = Booking.objects.create(
                    user=self.request.user,
                    trip=trip,
                    name=self.request.user.first_name,
                    surname=self.request.user.last_name,
                    date_joined=self.request.user.date_joined,
                )

                booking.save()
                return HttpResponse(booking)
        else:
            return HttpResponse(f'This trip cannot be booked, or is unavailable . Sorry')


@login_required(login_url='booking:login')
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_inventory = Inventory.objects.all().count()

    # Available
    num_instances_available = Inventory.objects.filter(remaining_count__exact=1).count() + \
                              Inventory.objects.filter(remaining_count__exact=2).count() + \
                              Inventory.objects.filter(remaining_count__exact=3).count() + \
                              Inventory.objects.filter(remaining_count__exact=4).count() + \
                              Inventory.objects.filter(remaining_count__exact=5).count()

    # The 'all()' is implied by default.
    num_members = Booking.objects.count()

    context = {
        'num_inventory': num_inventory,
        'num_instances_available': num_instances_available,
        'num_members': num_members,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('booking:home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'User was successfully created: {user}')
                return redirect('booking:login')
        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('booking:home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('booking:home')
            else:
                messages.info(request, 'Username or Password is Incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('booking:login')



