# Generated by Django 4.2.9 on 2024-02-23 14:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_remove_registeredevent_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredevent',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
