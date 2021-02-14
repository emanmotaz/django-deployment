from django.db import models
# to import user model
from django.contrib.auth.admin  import User
# Create your models here.
class UserProfileInfo(models.Model):
    """docstring for UserProfileInfo."""
    # this is user to add additional fields to the users table
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    # additional fields
    portfolio_site = models.URLField(max_length=200,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username
