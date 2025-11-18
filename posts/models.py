"""
Models for posts app in django

"""

from django.db import models
from authentification.models import Account

# Create your models here.

class Post(models.Model):
    """
    Description of Post entity in database
    """
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='posts')
    content = models.CharField(max_length=500)
    likes = models.IntegerField(default=0, null=False)
