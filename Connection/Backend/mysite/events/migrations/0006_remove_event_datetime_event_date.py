# Generated by Django 4.2.9 on 2024-02-09 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_event_date_event_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='datetime',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]