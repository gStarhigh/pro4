# Generated by Django 3.2.20 on 2023-07-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20230714_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonbooking',
            name='lesson_time',
            field=models.TimeField(default='18:00'),
        ),
    ]
