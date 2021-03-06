from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from .managers import CustomUserManager
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    


    
class ArtistData(models.Model):
    image = models.CharField(max_length=1255,null=True) 
    name = models.CharField(max_length=1255,null=True)
    stats = models.CharField(max_length=10255,null=True)
   
    def __str__(self):
        return self.name 
    
    def save_artist(self):
        self.save()