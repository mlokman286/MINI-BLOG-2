from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='pics',null=True)
    date = models.DateField(null=True,auto_now_add=True)
    time =models.TimeField( auto_now=False, auto_now_add=True)