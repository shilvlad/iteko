from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class HelpDeskRoles(models.Model):
    ROLES_CHOICES = (
        ('user', 'Пользователь'),
        ('serviceman', 'Сервисный инженер'),
        ('admin', 'Администратор')
    )
    role = models.CharField(max_length = 100, choices = ROLES_CHOICES)

    def __str__(self):
        return self.role


class HelpDeskUsers(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    role = models.ManyToManyField(HelpDeskRoles)
    def __str__(self):
        return self.user.username

class HelpDeskIncidents(models.Model):
    INCIDENT_TYPES_CHOICES = (
        ('soft', 'Программный сбой'),
        ('zip', 'Расходные материалы'),
        ('crq', 'Запрос на изменение')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_type = models.CharField(max_length=100, choices=INCIDENT_TYPES_CHOICES)
    description = models.TextField(max_length = 3000)
    timestamp_created = models.DateTimeField(editable=False, blank=True, auto_now_add=True)


