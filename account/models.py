from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=50)
    salary=models.IntegerField()
    age=models.IntegerField()
    city=models.CharField(max_length=50)

def __str__(self):
    return self.name