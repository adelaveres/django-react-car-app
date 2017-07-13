from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    engine = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

