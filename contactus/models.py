from django.db import models
from sqlalchemy import false

# Create your models here.

class Message(models.Model):

    name = models.CharField(max_length=30,null=False,blank=False)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100,null=False,blank=False)
    message = models.TextField()


    def __str__(self):
        return self.name