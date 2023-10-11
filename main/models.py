from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='users/', blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    img = models.ImageField(upload_to='news_photo/')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class About_us(models.Model):
    title = models.CharField(max_length=255)
    text_1 = models.TextField()
    text_2 = models.TextField()

    def __str__(self):
        return self.title


class Our_team(models.Model):
    img = models.ImageField(upload_to='team/')
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name











