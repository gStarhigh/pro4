from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_booking_date(value):
    """
    Checks if the bookings date is valid. Valid days are Monday
    to Friday.
    """
    if value.weekday() > 4:  # Monday = 0, Friday = 4
        raise ValidationError("Bookings are only allowed"
                              "on Mondays to Fridays.")
    if value < timezone.now().date():
        raise ValidationError("Booking date cannot be in the past.")


def validate_booking_time(value):
    """
    Checks if the booking time is valid. Valid booking time is 18-21.
    """
    allowed_times = [time(18, 0), time(19, 0), time(20, 0), time(21, 0)]
    if value not in allowed_times:
        raise ValidationError("Invalid booking time")
