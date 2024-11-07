from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=12)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=120)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    size = models.DecimalField(max_digits=13, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title