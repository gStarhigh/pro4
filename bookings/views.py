from django.shortcuts import render
from django.views import generic, View
from .forms import LessonBookingForm


class Home(generic.TemplateView):
    """ This view is used to display the home page """
    template_name = "index.html"


class LessonBooking(View):
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
            return redirect('my_bookings')

        return render(request, self.template_name, {'form': form})


class CalendarView(View):
    def get(self, request):
        # Get the booking data from the database
        bookings = LessonBooking.objects.all()

        # Create a list of the bookings
        events = []
        for booking in bookings:
            event = {
                'title': booking.user.username,
                'start': booking.lesson_date.isoformat(),
                'end': booking.lesson_date.isoformat(),
                'color': 'green' if booking.booking_status == 1 else 'red',
            }
            events.append(event)

        return JsonResponse(events, safe=False)
