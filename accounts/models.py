from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    stripe_customer_id = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    perfil_photo = models.ImageField(upload_to='images/accounts',verbose_name='Foto de Perfil')
    points = models.IntegerField(default=0)