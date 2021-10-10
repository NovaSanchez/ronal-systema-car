from django.db import models
from django.db.models.fields import EmailField

# Create your models here.


class Customer(models.Model):

    cedula = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    direction = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone =  models.CharField(max_length=50)


    def __str__(self):
        return "%s - %s  - %s"%(self.first_name, self.last_name, self.cedula)


