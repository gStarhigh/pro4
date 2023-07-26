from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .forms import LessonBookingForm, UpdateLessonBookingForm, DeleteBooking
from .models import LessonBooking
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from .validation import validate_booking_deletion
from django.core.exceptions import ValidationError


class Home(generic.TemplateView):
    """ This view is used to display the home page """
    template_name = "index.html"


class CreateLessonBooking(View):
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
        return LessonBooking.objects.filter(user=self.request.user,
                                            lesson_date__gte=today)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_bookings'] = context['object_list']
        return context


class DeleteBooking(View):
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


class UpdateBooking(View):
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
