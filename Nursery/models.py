from django.contrib.auth.models import User
from Plant.models import Plant
from django.db import models

# Create your models here.

class MyNursery(models.Model):
    shopName = models.TextField()
    seller = models.ForeignKey(User, on_delete = models.CASCADE)
    shopAddress = models.TextField()
    contact = models.BigIntegerField(null = False)

    def __str__(self):
        return self.shopName

class NurseryCollection(models.Model):
    plant = models.ForeignKey(Plant, on_delete = models.CASCADE)
    nursery = models.ForeignKey(MyNursery, on_delete = models.CASCADE)

    def __str__(self):
        return f'Collections of {self.nursery.shopName}'
