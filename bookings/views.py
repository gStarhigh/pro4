from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic import (TemplateView, DeleteView, UpdateView,
                                  DetailView, ListView)
from django.views import generic, View
from .forms import (LessonBookingForm, UpdateLessonBookingForm, DeleteBooking,
                    ContactForm)
from .models import LessonBooking
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib import messages
from .validation import validate_booking_deletion
from django.core.exceptions import ValidationError
from equestrian import settings


# Home Page View
class Home(TemplateView):
    """ Display the home page """
    template_name = 'index.html'


# About Page View
class About(TemplateView):
    """
    Display the about page.
    Fetch the Google Maps API Key from Settings.py, obtained from env.py.
    """
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['api_key'] = settings.GOOGLE_SECRET
        return context


# Account Details View
class AccountDetails(LoginRequiredMixin, TemplateView):
    """
    Display User account details and allow for updates.
    """
    def get(self, request):
        return render(request, 'details.html', {'user': request.user})

    def post(self, request):
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        messages_list = []

        if first_name != user.first_name:
            user.first_name = first_name
            user.save()
            messages_list.append('Your First name has been updated!')

        if last_name != user.last_name:
            user.last_name = last_name
            user.save()
            messages_list.append('Your Surname has been updated')

        if email != user.email:
            user.email = email
            user.save()
            messages_list.append('Your Email address has been updated')

        if messages_list:
            messages.info(request, ' '.join(messages_list))

        return redirect('account_details')


# Contact Page View
class Contact(FormView):
    """
    Display the Contact page and handle form submission.
    """
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('Home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = (self.request.user
                          if self.request.user.is_authenticated else None)
        return kwargs

    def form_valid(self, form):
        messages.info(self.request, 'Your message was sent successfully!')
        return super().form_valid(form)


# Create Lesson Booking View
class CreateLessonBooking(LoginRequiredMixin, TemplateView):
    """
    Display the booking page and handle lesson booking submission.
    """
    template_name = 'create_booking.html'

    def get(self, request):
        form = LessonBookingForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LessonBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.info(request, 'Your lesson was booked successfully!')
            return redirect('my_bookings')

        return render(request, self.template_name, {'form': form})


# User's Booked Lessons View
class MyBookings(LoginRequiredMixin, ListView):
    """ This view is used to display the users booked lessons """
    template_name = 'my_bookings.html'
    model = LessonBooking

    def get_queryset(self):
        today = timezone.now().date()
        booking_status = self.request.GET.get('booking_status')

        if booking_status == 'upcoming':
            return LessonBooking.objects.filter(
                user=self.request.user,
                lesson_date__gte=today,
                booking_status=1
            )
        elif booking_status == 'completed':
            return LessonBooking.objects.filter(
                user=self.request.user,
                lesson_date__lt=today,
                booking_status=1
            )
        else:
            return LessonBooking.objects.filter(
                user=self.request.user
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_bookings'] = context['object_list']
        return context


# Delete Booking View
class DeleteBooking(LoginRequiredMixin, DeleteView):
    """
    This view is used to confirm the deletion of a booking or throw an error.
    """
    template_name = 'delete_booking.html'

    def get(self, request, booking_id):
        booking = get_object_or_404(LessonBooking, booking_id=booking_id,
                                    user=request.user)
        return render(request, self.template_name, {'booking': booking})

    def post(self, request, booking_id):
        booking = get_object_or_404(LessonBooking, booking_id=booking_id,
                                    user=request.user)

        if 'confirmation' in request.POST:
            try:
                validate_booking_deletion(booking)
                booking.delete()
                messages.success(request, 'Your lesson was successfully'
                                          ' deleted!')
                return redirect('my_bookings')
            except ValidationError as e:
                messages.error(request, e.message)
                return redirect('my_bookings')
        else:
            messages.error(request, 'Booking not deleted.')
            return redirect('my_bookings')


# Update Booking View
class UpdateBooking(LoginRequiredMixin, UpdateView):
    """
    This view is used to update the booking of a lesson.
    """
    template_name = 'update_booking.html'

    def get(self, request, booking_id):
        booking = get_object_or_404(LessonBooking, booking_id=booking_id,
                                    user=request.user)
        form = UpdateLessonBookingForm(instance=booking)
        return render(request, self.template_name,
                      {'form': form, 'booking': booking})

    def post(self, request, booking_id):
        booking = get_object_or_404(LessonBooking, booking_id=booking_id,
                                    user=request.user)
        form = UpdateLessonBookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.info(request, 'Your lesson was updated successfully!')
            return redirect('my_bookings')
        return render(request, self.template_name,
                      {'form': form, 'booking': booking})
