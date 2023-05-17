from django.db import models
from django.contrib.auth.models import AbstractUser

app_name = 'accounts'

class CustomUser(AbstractUser):
    tel = models.CharField(max_length=15, null=True, blank=True)
    user_image = models.ImageField(upload_to='user',default='default.jpg')


