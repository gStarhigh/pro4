from django import forms
from .models import LessonBooking
from django.core.validators import MaxValueValidator
from django.utils import timezone
from .validation import (validate_booking_date, validate_booking_time,
                         validate_booking_deletion)
from datetime import time
from django.db.models import Sum


class LessonBookingForm(forms.ModelForm):
    NO_PARTICIPANTS_CHOICES = [(i, str(i)) for i in range(1, 4)]

    class Meta:
        model = LessonBooking
        fields = ['focus_lesson', 'lesson_date', 'lesson_time',
                  'no_participants', 'level_ekipage', 'terms_checked']
        widgets = {
            'focus_lesson': forms.Textarea(attrs={'cols': 30, 'rows': 10}),
            'lesson_date': forms.DateInput(attrs={'type': 'date', 'min':
                                                  timezone.now()
                                                  .strftime('%Y-%m-%d')}),
            'lesson_time': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'lesson_date': 'Available days are Monday to Friday',
            'lesson_time': 'Choose a time between 18:00 and 21:00.',
            'focus_lesson': 'Enter the focus for your lesson:',
            'terms_checked': 'I have read and understood the terms',
            'level_ekipage': 'Choose your level:',
        }
    no_participants = forms.ChoiceField(choices=NO_PARTICIPANTS_CHOICES,
                                        widget=forms.Select)

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
        no_participants_str = cleaned_data.get('no_participants')

        if lesson_date and lesson_time and no_participants_str:
            no_participants = int(no_participants_str)
            booking_datetime = timezone.make_aware(
                timezone.datetime.combine(lesson_date, lesson_time)
            )
            existing_bookings = LessonBooking.objects.filter(
                lesson_date=booking_datetime.date(),
                lesson_time=booking_datetime.time(),
            ).exclude(pk=self.instance.pk)

            total_participants = existing_bookings.aggregate(
                Sum('no_participants')).get('no_participants__sum', 0)

            if total_participants is None:
                total_participants = 0

            available_slots = 3 - total_participants

            if available_slots < no_participants:
                raise forms.ValidationError("Booking is full for the "
                                            "selected date and time.")
        return cleaned_data


class DeleteBooking(forms.Form):
    confirmation = forms.BooleanField(
        required=True,
        widget=forms.HiddenInput(attrs={"value": True})
    )

    def clean(self):
        cleaned_data = super().clean()
        confirmation = cleaned_data.get('confirmation')

        if confirmation:
            booking_id = self.instance
            try:
                booking = LessonBooking.objects.get(pk=booking_id)
                validate_booking_deletion(booking)
            except LessonBooking.DoesNotExist:
                raise forms.ValidationError("Booking not found.")
        else:
            raise forms.ValidationError("You must confirm the deletion.")

        return cleaned_data


class UpdateLessonBookingForm(forms.ModelForm):
    """
    Form for updating the Booked lesson.
    """
    NO_PARTICIPANTS_CHOICES = [(i, str(i)) for i in range(1, 4)]

    class Meta:
        model = LessonBooking
        fields = ['focus_lesson', 'lesson_date', 'lesson_time',
                  'no_participants', 'level_ekipage', 'terms_checked']
        widgets = {
            'focus_lesson': forms.Textarea(attrs={'cols': 30, 'rows': 10}),
            'lesson_date': forms.DateInput(attrs={'type': 'date', 'min':
                                                  timezone.now()
                                                  .strftime('%Y-%m-%d')}),
            'lesson_time': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'focus_lesson': 'Enter the focus for your lesson:'
        }
    no_participants = forms.ChoiceField(choices=NO_PARTICIPANTS_CHOICES,
                                        widget=forms.Select)

    def clean(self):
        cleaned_data = super().clean()
        lesson_date = cleaned_data.get('lesson_date')
        lesson_time = cleaned_data.get('lesson_time')
        no_participants_str = cleaned_data.get('no_participants')

        if lesson_date and lesson_time and no_participants_str:
            no_participants = int(no_participants_str)
            booking_datetime = timezone.make_aware(
                timezone.datetime.combine(lesson_date, lesson_time)
            )
            existing_bookings = LessonBooking.objects.filter(
                lesson_date=booking_datetime.date(),
                lesson_time=booking_datetime.time(),
            ).exclude(pk=self.instance.pk)

            total_participants = existing_bookings.aggregate(
                Sum('no_participants')).get('no_participants__sum', 0)

            if total_participants is None:
                total_participants = 0

            available_slots = 3 - total_participants

            if available_slots < no_participants:
                raise forms.ValidationError("Booking is full for the "
                                            "selected date and time.")
        return cleaned_data


class ContactForm(forms.Form):
    """
    Contact form for the user to contact the page owner.
    """
    fields = ['name', 'email', 'subject', 'message']
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        # Get the info from the logged in user, if they exist.
        user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)

        # If the user is logged in, get the name and email and make
        # the fields readonly.
        if user and user.is_autheticated:
            self.fields['name'].initial = user.username
            self.fields['email'].initial = user.email
            self.fields['name'].widget.attrs['readonly'] = True
            self.fields['email'].widget.attrs['readonly'] = True
