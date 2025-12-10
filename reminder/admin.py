from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display =[
        'message'
    ]