from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Ideas(models.Model):
    idea = models.CharField(max_length=1200)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
