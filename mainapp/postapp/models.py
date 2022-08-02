from distutils.command.upload import upload
from tkinter import Image
from tkinter.tix import Tree
from django.db import models
from django.forms import ImageField
from accountapp.models import User

# Create your models here.

class Tweet(models.Model):
    Text      = models.CharField(max_length=50)
    Img       = models.ImageField(upload_to='images')
    Upload_dt = models.DateField(auto_now=True)
    Edit_dt   = models.DateField(auto_now=True)
    Owner     = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER')