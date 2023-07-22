from django import forms
from .models import LessonBooking
from django.core.validators import MaxValueValidator
from django.utils import timezone
from .validation import validate_booking_date, validate_booking_time
from datetime import time
from django.db.models import Sum


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
        no_participants = cleaned_data.get('no_participants')

        if lesson_date and lesson_time and no_participants:
            booking_datetime = timezone.make_aware(
                timezone.datetime.combine(lesson_date, lesson_time)
            )
            existing_bookings = LessonBooking.objects.filter(lesson_date=booking_datetime)
            total_participants = existing_bookings.aggregate(Sum('no_participants'))['no_participants__sum'] or 0
            available_slots = 3 - total_participants

            if available_slots < no_participants:
                raise forms.ValidationError("Booking is full for the selected date and time.")
        return cleaned_data
