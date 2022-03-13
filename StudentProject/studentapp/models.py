from pyexpat import model
from statistics import mode
from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    city = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    sname = models.CharField(max_length=80)
    age = models.IntegerField()
    standard = models.CharField(max_length=20)
    div = models.CharField(max_length=5)
    School = models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return self.sname
    