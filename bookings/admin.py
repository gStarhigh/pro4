from django.contrib import admin
from .models import LessonBooking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(LessonBooking)
class LessonAdmin(SummernoteModelAdmin):
    summernote_fields = ('focus_lesson')
    list_display = ('booking_id', 'user', 'lesson_date', 'lesson_time',
                    'no_participants', 'created_on', 'booking_status')
    search_fields = ('user', 'lesson_date', 'lesson_time', 'booking_status')
    list_filter = ('user', 'lesson_date', 'lesson_time', 'booking_status')
    actions = ['approve_lesson']

    def approve_lesson(self, request, queryset):
        queryset.update(booking_status=1)

        """
        Send an email to the user when the booking has been approved,
        using emailJS.
        """
        for booking in queryset:
            user = booking.user
            subject = "Your booking has been approved."
            message = f"Hello {user.username}. Your lesson has been approved."
            f"Date: {lesson_date}"
            f"Time: {lesson_time}"
            "We look forward to seeing you!"
            from_email = "starhog.gard@gmail.com"
            to_email = [user.email]
