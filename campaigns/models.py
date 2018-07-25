from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

from django import template
register = template.Library()

class Campaign(models.Model):
    user = models.ForeignKey(User, related_name = 'user_campaign', on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username
