from Nursery.models import MyNursery
from .cart import CustomerCart
from django.db import models


class PlaceOrder(models.Model):
    customer = models.ForeignKey(CustomerCart, on_delete = models.CASCADE)
    shopId = models.IntegerField(default=0)
    orderedAt = models.DateTimeField(auto_now_add = True)
    address = models.TextField()
    phone = models.BigIntegerField(null = False)
    success = models.BooleanField(default = False)
    total = models.FloatField(default = 0)

    def __str__(self):
        return self.customer.customer.username

    def save(self, *args, **kwargs):
        self.success = True
        self.total = self.customer.total
        self.shopId = self.customer.shopFrom.id
        super(PlaceOrder, self).save(*args, **kwargs)
