from django import forms
from .models import LessonBooking


class LessonBookingForm(forms.ModelForm):
    class Meta:
        model = LessonBooking
        fields = ['focus_lesson', 'lesson_date', 'lesson_time',
                  'terms_checked', 'no_participants', 'level_ekipage']
        widgets = {
            'lesson_date': forms.DateInput(attrs={'type': 'date'}),
            'lesson_time': forms.TimeInput(attrs={'type': 'time'}),
        }
