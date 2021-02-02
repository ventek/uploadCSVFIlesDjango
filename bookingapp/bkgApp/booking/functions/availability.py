from booking.models import Inventory, Booking


def trip_availability(inventory, data, booking_count):

    MAX_BOOKINGS = 2
    field_name = 'remaining_count'
    obj_i = Inventory.objects.filter(title=data).first()
    remaining_count = getattr(obj_i, field_name)

    avail_list = []
    booking_set = Booking.objects.filter(trip=inventory)
    for booking in booking_set:
        if booking.booking_count < booking_count or remaining_count < MAX_BOOKINGS:
            avail_list.append(True)
        else:
            avail_list.append(False)
    # true if all of the items in the list are true, it will return true
    return all(avail_list)




