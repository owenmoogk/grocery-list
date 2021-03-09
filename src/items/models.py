from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
    price = models.DecimalField(decimal_places = 2, max_digits=10000, null = True)
    owner = models.ForeignKey('auth.User', related_name='packages', on_delete=models.CASCADE, null=True)