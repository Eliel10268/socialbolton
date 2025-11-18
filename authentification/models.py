from django.db import models

# Create your models here.

class Account(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    
