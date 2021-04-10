from django.contrib.auth.models import User
from Plant.models import Plant
from django.db import models
import datetime
# Create your models here.

STATUS = (
 ("customer", "Customer"),
 ("seller", "Seller")
)

class User(models.Model):
    name = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.TextField(choices = STATUS)
    phone = models.BigIntegerField(null = False)

    def __str__(self):
        return self.name.username
