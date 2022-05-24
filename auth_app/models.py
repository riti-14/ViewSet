
from django.db import models

# Create your models here.
 

class Register(models.Model):
    name=models.CharField(max_length=50) 
    email=models.EmailField()
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    confirmpassword=models.CharField(max_length=10)


    def __str__(self):
        return self.name    