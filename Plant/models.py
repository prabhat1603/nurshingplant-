from django.db import models

# Create your models here.

STATUS = (
 ("tree", "Tree"),
 ("shrub", "Shrub"),
 ("herb", "Herb"),
 ("climber", "Climber"),
 ("creeper", "Creeper")
)



class Plant(models.Model):
    name = models.CharField(max_length = 50, null = False)
    type = models.TextField(choices = STATUS, default = "Tree")
    about = models.TextField(null = True)
    cost = models.FloatField(null = False)
    image = models.ImageField(upload_to = 'plantPic', null = False, blank = False, default = 'default.jpg')

    def __str__(self):
        return self.name
