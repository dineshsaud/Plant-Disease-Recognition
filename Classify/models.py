from django.db import models

# Create your models here.


class testImage(models.Model):
    image = models.ImageField(upload_to='leaf_image',blank=True)
    
class DiseaseDes(models.Model):
    name=models.CharField(max_length=250)
    cause=models.CharField(max_length=100)
    chemical=models.CharField(max_length=250)
    suggestion=models.CharField(max_length=250)