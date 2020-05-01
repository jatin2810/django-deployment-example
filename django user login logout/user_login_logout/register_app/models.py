from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):

    # user is instance of User model
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    ##additional information added to User and name the model UserProfileInfo

    portfolio_link=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username
        ##username is the field inside User
