from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField
    registration = models.CharField(max_length=20)

    def __str__(self):
        return self.name
