from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField()
    price = models.DecimalField(decimal_places = 2, max_digits=10000, null = True)
