from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    #image = models.ImageField(upload_to='pics')
    status= models.BooleanField(default=False)