from django.db import models
from django.conf import settings
# Create your models here.

class Reminder(models.Model):
    FREQUENCY_CHOICES =[
        ('once', 'Once'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    remind_at = models.DateTimeField()
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES, default='once')

    def __str__(self):
        return f"{self.message} at {self.remind_at}"