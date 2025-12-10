from celery import shared_task
from time import sleep
from django.utils import timezone
from .models import Reminder

@shared_task
def send_reminder(user_id=None):
    now= timezone.now()
    if user_id:
        reminder = Reminder.objects.filter(user_id=user_id, remind_at__lte=now)
    else:
        reminder = Reminder.objects.filter(remind_at__lte=now)
    
    for r in reminder:
        print(f"Reminder for user {r.user.id} ({r.user.username}): {r.message}")

        if r.frequency == 'daily':
            r.remind_at += timezone.timedelta(days=1)
            r.save()
        elif r.frequency == 'weekly':
            r.remind_at += timezone.timedelta(weeks=1)
            r.save()

        elif r.frequency == 'once':
            
            r.delete()
        else:
            r.delete()

        sleep(3)
    
    return f"Processed reminders" + (f"for user {user_id}" if user_id else "")
