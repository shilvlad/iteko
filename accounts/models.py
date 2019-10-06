from django.db import models

# Create your models here.

class AccountsRegistrationRequest(models.Model):
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    
