# Create your models here.
from django.db import models

class data4(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Qualification = models.CharField(max_length=100)
    Yearofpass = models.IntegerField()
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    post = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

