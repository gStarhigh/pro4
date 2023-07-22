from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
import uuid


BOOKING_STATUS = ((0, "Awaiting Approval"), (1, "Confirmed"))


class LessonBooking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                  editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_booking")
    updated_on = models.DateField(auto_now_add=True)
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
        ordering = ["-lesson_date"]

    def __str__(self):
        return str(self.booking_id)
