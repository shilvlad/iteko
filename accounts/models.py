from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return 'Профиль: ' + self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        ProfileBasicSettings.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ProfileBasicSettings(models.Model):
    SERVICES_CHOICES = (
        ('helpdesk', 'Help Desk'),
        ('taxi', 'Сервис Такси'),
        ('main', 'Главная страница'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_service = models.CharField(max_length=100, choices=SERVICES_CHOICES, default='main')
    def __str__(self):
        return 'Базовые настройки: ' + self.user.username

class AccountsRegistrationRequest(models.Model):
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
