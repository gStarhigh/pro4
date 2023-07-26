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
        queryset.update(approved=True)
