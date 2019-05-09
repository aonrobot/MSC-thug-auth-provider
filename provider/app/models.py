from django.db import models

# Create your models here.

class Application(models.Model):
    app_name = models.CharField(max_length=100)
    redirect_uri = models.CharField(max_length=100, default="")
