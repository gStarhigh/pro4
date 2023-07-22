from django.shortcuts import render, redirect
from django.views import generic, View
from .forms import LessonBookingForm
from .models import LessonBooking


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
            return redirect('Home')

        return render(request, self.template_name, {'form': form})
