from django.db import models

# Create your models here.

class mylogs(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    ip_address = models.TextField(max_length=100)
    port = models.TextField(max_length=100)
    http_response = models.TextField(max_length=100)