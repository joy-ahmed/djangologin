from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    profileImg = models.ImageField(upload_to="images/", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
