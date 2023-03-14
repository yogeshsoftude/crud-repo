from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
   

    def __str__(self):
        return self.name 

class Reg(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)    

    def __str__(self):
        return self.first_name

    