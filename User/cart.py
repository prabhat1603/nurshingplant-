from django.contrib.auth.models import User
from Nursery.models import MyNursery
from django.utils import timezone
from Plant.models import Plant
from django.db import models



# If user is customer
class CustomerCart(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    addTocart_on = models.DateField(auto_now_add = True)
    plant = models.ForeignKey(Plant, on_delete = models.CASCADE)
    shopFrom = models.ForeignKey(MyNursery, on_delete = models.CASCADE, default = 1)
    quantity = models.IntegerField(default = 1)
    total = models.FloatField(default = 0)

    def __str__(self):
        return f'Cart of {self.customer.username}'

    def save(self, *args, **kwargs):
       self.total = self.quantity * self.plant.cost
       super().save(*args, **kwargs)
