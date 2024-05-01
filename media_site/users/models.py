from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt import RefreshToken

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 
        
options = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others','Others')
    )

class User(AbstractUser,BaseModel):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    gender = models.CharField(
        choices = options,
        default = 'male',
        null=False,
        blank=False
        )
    bio = models.TextField(max_length=500, blank=True)
    profile_pic= models.ImageField(upload_to='profile_images/',null=True,blank=True)
    dob = models.DateField(max_length=8,blank=False)
    
    def __str__(self):
        return self.username
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }