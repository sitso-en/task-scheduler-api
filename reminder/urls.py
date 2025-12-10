from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('user_reminders', views.ReminderViewSet, basename= 'user_reminders')

urlpatterns = router.urls