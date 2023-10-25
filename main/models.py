from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    bio = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.ImageField(upload_to='user-avatar/', null=True, blank=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Banner(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    desription = models.CharField(max_length=55)
    img = models.ImageField(upload_to='banner_photos/')

    def __str__(self):
        return self.title


class Info(models.Model):
    logo = models.ImageField(upload_to='logo_photos/')
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    lat = models.FloatField(null=True, blank=True, default=0)
    lot = models.FloatField(null=True, blank=True, default=0)
    email = models.CharField(max_length=55,null=True, blank=True, default=0)

    def __str__(self):
        return self.phone_number


class About(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=255)
    img = models.ImageField(upload_to='banners_photos/')

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='service_icon/')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    img = models.ImageField(upload_to='meal_photos/')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    icon = models.ImageField(upload_to='test/')
    name = models.CharField(max_length=255)
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Client(models.Model):
    img = models.ImageField(upload_to='client_photos/')


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    message = models.TextField()
    email =models.CharField(max_length=55, null=True, blank=True)
    subject = models.CharField(max_length=55, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Chef(models.Model):
    name = models.CharField(max_length=25)
    img = models.ImageField(upload_to='chef_photos/')
    job = models.CharField(max_length=25)
    about_chef = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Block(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='block_photos/')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title