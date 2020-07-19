from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=30,default="")
    state = models.CharField(max_length=30,default="")
    city = models.CharField(max_length=50,default="")



