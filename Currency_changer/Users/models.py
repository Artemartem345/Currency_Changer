from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
class AccountManager(BaseUserManager):
    def create_superuser(self, email, password, firstname, lastname, **other_fields):        
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)        
        other_fields.setdefault("is_admin", True)
        other_fields.setdefault("is_superuser", True)        
        if other_fields.get('is_staff') is not True:
            raise ValueError("is_staff must be True")       
        if other_fields.get('is_superuser') is not True:
            raise ValueError("is_superuser must be True")        
        return self.create_user(email, password, firstname, lastname, **other_fields)
    def create_user(self, email, password, firstname, lastname, **other_fields):
        email = self.normalize_email(email)        
        user = self.model(email=email, firstname=firstname, lastname=lastname,
                          **other_fields)        
        user.set_password(password)
        user.save()        
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):    
    email = models.EmailField(('email address'), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)    
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)    
    room_number = models.IntegerField(null=True)
    is_staff = models.BooleanField(default=False)    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)
    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']
    def __str__(self):        
        return self.firstname + ' ' + self.lastname +f', комната: {self.room_number}'
    