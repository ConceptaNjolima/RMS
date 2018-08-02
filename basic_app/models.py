from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


# Create your model with the extra fields needed.
class UserProfileInfo(models.Model):
    # create a relationship with the user model*do not inherit
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    # Add additional attributes
    Number = models.IntegerField(default=20)

    def __str__(self):
        return self.user.username
