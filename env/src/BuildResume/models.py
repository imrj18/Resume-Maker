from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.db import models

class user(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, primary_key=True)
    password = models.CharField(max_length=20, blank=False, null=False)
    mail = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)  # Updated to CharField
    #image_path = models.ImageField(upload_to='profile_images/', null=True, blank=True)