# Generated by Django 4.2.9 on 2024-02-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_rename_event_registeredevent_event_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeredevent',
            name='user',
        ),
        migrations.AddField(
            model_name='registeredevent',
            name='username',
            field=models.CharField(default='default_user', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registeredevent',
            name='event_name',
            field=models.CharField(max_length=255),
        ),
    ]
