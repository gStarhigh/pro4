from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
import uuid

# Booking status of the Lesson
BOOKING_STATUS = ((0, "Awaiting Approval"), (1, "Confirmed"))


# Lesson model
class LessonBooking(models.Model):
    """
    Represents a lesson booking made by a user.

    Attributes:
        booking_id (UUID): The unique identifier for the booking.
        user (User): The user who made the booking.
        updated_on (Date): The date when the booking was last updated.
        created_on (Date): The date when the booking was created.
        focus_lesson (str): Description of the focus of the lesson.
        lesson_date (Date): The date of the lesson.
        lesson_time (Time): The time of the lesson (default is 18:00).
        terms_checked (bool): Indicates if the user has checked the terms.
        no_participants (int): Number of participants (up to 3).
        level_ekipage (str): The level of the ekipage.
        booking_status (int): The status of the booking
                            (0: Awaiting Approval, 1: Confirmed).

    Meta:
        ordering (list): The order in which lesson bookings are displayed.
    """

    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                  editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_booking")
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)
    focus_lesson = models.TextField()
    lesson_date = models.DateField(auto_now=False)
    lesson_time = models.TimeField(default="18:00")
    terms_checked = models.BooleanField(default=False)
    no_participants = models.PositiveIntegerField(default=1,
                                                  validators=[MaxValueValidator
                                                              (3)])
    LEVEL_CHOICES = (
        ("Lätt C", "Lätt C"),
        ("Lätt B", "Lätt B"),
        ("Lätt A", "Lätt A"),
        ("MSV C", "MSV C"),
        ("MSV B", "MSV B"),
        ("MSV A", "MSV A"),
        ("Grand Prix", "Grand Prix"),
    )
    level_ekipage = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)

    class Meta:
        ordering = ["lesson_date"]

    def __str__(self):
        return str(self.booking_id)
