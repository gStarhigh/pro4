from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
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


class Home(generic.TemplateView):
    """ This view is used to display the home page """
    template_name = 'index.html'


class About(generic.TemplateView):
    """ This view is used to display the about page,
    and gets the Google Maps API key from Settings.py that gets it from env.py.
    This way keeping it safe and not published.
    """
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['api_key'] = settings.GOOGLE_SECRET
        return context


class AccountDetails(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'details.html', {'user': request.user})

    def post(self, request):
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        return redirect('account_details')


class Contact(FormView):
    """ This view is used to display the Contact page """
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


class CreateLessonBooking(LoginRequiredMixin, View):
    """ This view is used to display the booking page """
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


class MyBookings(LoginRequiredMixin, generic.ListView):
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


class DeleteBooking(LoginRequiredMixin, View):
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


class UpdateBooking(LoginRequiredMixin, View):
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
