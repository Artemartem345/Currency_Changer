from django.db import models

# Create your models here.


class Rubbish(models.Model):
    pass


class Food(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    img = models.ImageField(null=True, blank=True)
    href = models.CharField(max_length=130)
     
