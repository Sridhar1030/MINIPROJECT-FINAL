# Generated by Django 4.2.9 on 2024-03-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_subevent_end_time_subevent_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subevent',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='subevent',
            name='start_time',
        ),
        migrations.AddField(
            model_name='subevent',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]