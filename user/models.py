from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=150)
    username = models.CharField(
        max_length=150,
        unique=False,
        null=True,
        blank=True)
                               

    def __str__(self):
        return self.name
    
# Add related_name to groups and user_permissions fields
CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_set'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_set'
