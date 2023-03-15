from django.db import models

# Create your models here.

class mylogs(models.Model):
    time = models.TextField(max_length=100)
    name = models.TextField(max_length=100)
    ip_address = models.TextField(max_length=100)
    massage = models.TextField(max_length=2000)
