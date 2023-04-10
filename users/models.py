from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True , blank=True)
    name = models.CharField(max_length=200 , blank=True  , null=True)
    email = models.EmailField(max_length=200 , blank=True , null=True)
    username = models.CharField(max_length=200 , blank=True  , null=True)
    short_intro =  models.CharField(max_length=200 , blank=True  , null=True)
    bio = models.TextField(blank=True , null=True)
    profile_image = models.ImageField(blank=True ,null=True , upload_to='profiles/' , default='profiles/user-default.png')    
    social_github = models.CharField(max_length=200 , blank=True  , null=True)
    social_telegram = models.CharField(max_length=200 , blank=True  , null=True)
    social_instagram = models.CharField(max_length=200 , blank=True  , null=True)
    social_linkedin = models.CharField(max_length=200 , blank=True  , null=True)
    social_twitter = models.CharField(max_length=200 , blank=True  , null=True)
    id = models.UUIDField(unique=True , default=uuid.uuid4 , primary_key=True , editable=False)


    def __str__(self):
        return str(self.user.username)

