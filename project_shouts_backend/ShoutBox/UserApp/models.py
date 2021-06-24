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

FRIEND_STATUS=(
    (0,'pending'),
    (1,'Accepted'),
    (2,'Declined'),
    (3,'Blocked'),
    (4,'Unfriend')
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
            return mark_safe('<img src="/media/imgs/default.jpg" width="50" height="50" />')
    
    image_tag.short_description = 'Image'



class Shouts(models.Model):
    ShoutsId=models.AutoField(primary_key=True)
    UserId=models.ForeignKey(Users, on_delete=models.CASCADE)
    DateCreated =models.DateTimeField(blank=True, null=True, default=now)
    TextContent=models.TextField(max_length=400)
    File=models.CharField(max_length=400)
    FileType=models.CharField(max_length=10)
    IsDeleted=models.BooleanField(null=True,default=False)
	

class Friends(models.Model):
    UserId=models.ForeignKey(Users, on_delete=models.CASCADE,related_name='user_id')
    FriendId=models.ForeignKey(Users, on_delete=models.CASCADE,related_name='friend_id')
    StatusCode=models.IntegerField(choices=FRIEND_STATUS,default=4)
    ActionUserId=models.ForeignKey(Users, on_delete=models.CASCADE,related_name='actionUser_id')
    DateCreated=models.DateTimeField(blank=True, null=True, default=now)

class Comments(models.Model):
	CommentId=models.AutoField(primary_key=True)
	ShoutsId=models.ForeignKey(Shouts, on_delete=models.CASCADE)
	UserId=models.ForeignKey(Users, on_delete=models.CASCADE)
	CommentContent=models.TextField(max_length=200)
	DateCreated=models.DateTimeField(blank=True, null=True, default=now)

class ReportedShouts(models.Model):
	ReportId=models.AutoField(primary_key=True)
	ShoutsId=models.ForeignKey(Shouts, on_delete=models.CASCADE)
	UserId=models.ForeignKey(Users, on_delete=models.CASCADE)
	ReportedDate=models.DateTimeField(blank=True, null=True, default=now)
	IsDeleted=models.BooleanField(null=True,default=False)

