from django.contrib import admin
from .models import LessonBooking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(LessonBooking)
class LessonAdmin(SummernoteModelAdmin):
    summernote_fields = ('focus_lesson')
