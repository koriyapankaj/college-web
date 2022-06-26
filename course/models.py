from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Course(models.Model):

    course_name = models.CharField(max_length=50)
    c_disc = models.TextField()
    c_image = models.ImageField(upload_to='pics')


    def __str__(self):
        return self.course_name