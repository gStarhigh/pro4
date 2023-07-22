from django import forms
from .models import LessonBooking
from django.core.validators import MaxValueValidator
from django.utils import timezone
from .validation import validate_booking_date, validate_booking_time
from datetime import time


class LessonBookingForm(forms.ModelForm):
    class Meta:
        model = LessonBooking
        fields = ['focus_lesson', 'lesson_date', 'lesson_time',
                  'terms_checked', 'no_participants', 'level_ekipage']
        widgets = {
            'lesson_date': forms.DateInput(attrs={'type': 'date'}),
            'lesson_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean_lesson_date(self):
        lesson_date = self.cleaned_data['lesson_date']
        validate_booking_date(lesson_date)
        return lesson_date

    def clean_lesson_time(self):
        lesson_time = self.cleaned_data['lesson_time']
        validate_booking_time(lesson_time)
        return lesson_time

    def clean(self):
        cleaned_data = super().clean()
        lesson_date = cleaned_data.get('lesson_date')
        lesson_time = cleaned_data.get('lesson_time')
        if lesson_date and lesson_time:
            booking_datetime = timezone.make_aware(
                timezone.datetime.combine(lesson_date, lesson_time)
            )
            if (LessonBooking.objects.filter(lesson_date=booking_datetime)
                             .count() >= 3):
                raise forms.ValidationError("Booking is full for the"
                                            " selected date and time.")
        return cleaned_data
