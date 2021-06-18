from django.db import models
from django.db.models.fields import EmailField
from django.utils.timezone import now
from django.utils.html import mark_safe
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

GENDER_STATUS = (
    ('Male','Male'),
    ('Female','Female')
)

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100,unique=True)
    MobileNo = models.BigIntegerField(unique=True, blank=True, null=True)
    Password = models.CharField(max_length=100)
    Gender = models.TextField(choices=GENDER_STATUS,default='',blank=True,null=True)
    DateOfBirth = models.DateField(null=True)
    ProfilePicURL = models.ImageField(upload_to='documents',blank=True,null=True)
    DateCreated =models.DateTimeField(blank=True, null=True, default=now)
    IsActive = models.BooleanField(null=True)

    def __str__(self):
        return self.UserName

    def image_tag(self):
        if self.ProfilePicURL:
            return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.ProfilePicURL))
        else:
            return mark_safe('<img src="/media/documents/default.jpg" width="50" height="50" />')
    
    image_tag.short_description = 'Image'
