from distutils.command.upload import upload
from enum import unique
from tkinter import image_names

from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from pkg_resources import require
from django.contrib.auth import get_user_model
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
from allauth.account.signals import email_confirmed

User = get_user_model()

# Create your models here.

#Main Page
class Header(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/main',verbose_name='Logo')
    number = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Cabecera")
        verbose_name_plural = ("Cabecera")

#other

def schedule_directory_path(instance,filename):
    return 'Sets/{0}/{1}'.format(instance.title, filename)

class Schedule(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100, unique=True,verbose_name='Link Automatico (NO MODIFICAR)')
    image_v = models.ImageField(upload_to=schedule_directory_path,verbose_name='Imagen vertical(Portada del Set)')
    image_h = models.ImageField(null=True,blank=True,upload_to=schedule_directory_path,verbose_name='Imagen Banner(Si se requiere)')
    active = models.BooleanField(default=False)
    image_v1 = models.ImageField(upload_to=schedule_directory_path,verbose_name='Imagen vertical Foto demostrativa 1')
    image_v2 = models.ImageField(upload_to=schedule_directory_path,verbose_name='Imagen vertical Foto demostrativa 2')
    image_v3 = models.ImageField(upload_to=schedule_directory_path,verbose_name='Imagen vertical Foto demostrativa 3')    
    content = RichTextField(null=True,blank=True,verbose_name='Contenido')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Set")
        verbose_name_plural = ("Sets")
    
class Placeholder(models.Model):
    title = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to='images/general',verbose_name='Imagen que se descargara')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Imagen negra")
        verbose_name_plural = ("Imagenes en negro")

#MODELO STRIPE

class Pricing(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    stripe_price_id = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=3, max_digits=7)
    currency = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name="subscipcion")
    created = models.DateTimeField(auto_now_add=True)
    stripe_subsciption_id = models.CharField(max_length=50)
    status = models.CharField(max_length=100)

    class Meta:
        ordering =['-created']

    def __str__(self):
        return self.user.email

    @property
    def is_active(self):
        return self.status == "active" or self.status == "trialing"

# COURSES
def user_directory_path(instance,filename):
    return 'courses/{0}/{1}'.format(instance.title, filename)

def chapter_directory_path(instance, filename):
    return 'courses/{0}/{1}/{2}'.format(instance.course, instance.title, filename)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "

class Courses(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True,verbose_name='Link Automatico (NO MODIFICAR)')
    authors = models.ManyToManyField(Author)
    image = models.ImageField(upload_to=user_directory_path,verbose_name='Imagen de portada del curso')
    video_course = models.FileField(upload_to=user_directory_path,verbose_name='Video Demo')
    published = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    short_des = RichTextField(null=True,blank=True,verbose_name='Descripcion Corta')
    Content = RichTextField(null=True,blank=True,verbose_name='Contenido del curso')
    pricing_tier = models.ManyToManyField(Pricing, blank=True)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

def post_email_confirmed(request, email_address, *args , **kwargs):
    user = User.objects.get(email = email_address.email)
    free_trial_pricing = Pricing.objects.get(name = 'Free Trial')
    subscription = Subscription.objects.create(
        user = user,
        pricing = free_trial_pricing
    )

    #crear cliente
    stripe_customer = stripe.Customer.create(
        email = user.email        
    )
    stripe_subscription = stripe.Subscription.create(
        customer = stripe_customer["id"],
        items=[{'price':'price_1M4oJCLkpd3BJqT81AdkmAyT'}],
        trial_period_days =7
    )

    subscription.status= stripe_subscription["status"]
    subscription.stripe_subsciption_id = stripe_subscription["id"]
    subscription.save()
    user.stripe_customer_id =stripe_customer["id"]
    user.save()
    
class Chapter(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True, null=True)
    chapter_number = models.IntegerField(blank=True,null=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=chapter_directory_path,verbose_name='Imagen de portada del capitulo')
    video_chapter = models.FileField(upload_to=chapter_directory_path,verbose_name='Video del Capitulo')
    content = RichTextField(null=True,blank=True,verbose_name='Contenido')

    def __str__(self):
        return self.title

email_confirmed.connect(post_email_confirmed)
