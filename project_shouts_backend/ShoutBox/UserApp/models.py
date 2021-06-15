from django.db import models
from django.db.models.fields import EmailField
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100,unique=True)
    # MobileNo = models.PhoneNumberField(null=False, blank=False, unique=True)
    MobileNo = models.BigIntegerField()
    Password = models.CharField(max_length=100)
    # Gender = models.CharField(max_length=100)
    DateOfBirth = models.DateField(null=True)
    # ProfilePicURL
    # DateCreated
    # IsActive
