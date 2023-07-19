from django import forms
from .models import LessonBooking


class LessonBookingForm(forms.ModelForm):
    class Meta:
        model = LessonBooking
        fields = ['focus_lesson', 'lesson_date', 'terms_checked',
                  'no_participants', 'level_ekipage']
