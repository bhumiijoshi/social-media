from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from media_site.models import BaseModel

class User(AbstractUser,BaseModel):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others','Others')
    )
    
    email = models.EmailField(max_length=255, unique=True, db_index=True,verbose_name = "Email")
    gender = models.CharField(
        choices = GENDER,
        default = 'male',
        null=False,
        blank=False,
        verbose_name = "Gender"
        )
    bio = models.TextField(blank=True,verbose_name = "Bio")
    profile_pic= models.ImageField(upload_to='profile_image/',null=True,blank=True,verbose_name = "Profile Picture")
    date_of_birth = models.DateField(max_length=8,blank=False,verbose_name = "Date Of Birth")
    
    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        
    def __str__(self):
        return self.username
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }