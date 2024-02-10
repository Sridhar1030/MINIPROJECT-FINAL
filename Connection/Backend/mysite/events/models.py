from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)  # First date field
    another_date = models.DateField(default=timezone.now)  # Second date field

    class Meta:
        app_label = 'events'

    def __str__(self):
        return self.name
