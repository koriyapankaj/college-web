from django.db import models

# Create your models here.

class Gallery(models.Model):

    g_title=models.CharField(max_length=50)
    g_disc=models.TextField()
    g_image=models.ImageField(upload_to='assets/pics')

    def __str__(self):
        return self.g_title
    
