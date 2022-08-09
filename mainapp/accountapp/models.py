from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Date_Of_Birth = models.DateField(null=True)
    Gender        = models.CharField(max_length=8)
    Phone_Num     = models.CharField(max_length=11)
    Profile       = models.FileField(upload_to="Profile/")