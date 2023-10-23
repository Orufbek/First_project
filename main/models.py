from django.db import models
from django.contrib.auth.models import AbstractUser


class Banner (models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=25)
    text = models.CharField(max_length=255)
    img = models.ImageField(upload_to='banner_img/')

    def __str__(self):
        return self.description

class User(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    bio = models.CharField(max_length=155)

    class Mete(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class About(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField()
    img = models.ImageField(upload_to='about_img/')



    def __str__(self):
        return self.title



class Servies(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='ser_icon/')


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)



    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=55)
    img = models.ImageField(upload_to='meal_photo/')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.name


class Client(models.Model):
    photo = models.ImageField(upload_to='client_photo')


class Tag (models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name


class Blog_Category(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(to=Blog_Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(to=Tag, blank=True)
    description = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='blog_photo')
    date = models.DateField(auto_now=True)


    def __str__(self):
        return self.title





class Contact(models.Model):
    firs_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    message = models.TextField()
    email = models.CharField(max_length=55, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.firs_name




class Info(models.Model):
    logo = models.ImageField(upload_to='brand_logo/')
    phone_number = models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    facebook = models.CharField(max_length=55)
    twitter = models.CharField(max_length=55)
    instagram = models.CharField(max_length=55)
    img = models.ImageField(upload_to='img/')
    lot = models.FloatField()
    lat = models.FloatField()
    email = models.CharField(max_length=55)



    def __str__(self):
        return self.phone_number


class Chef(models.Model):
    name = models.CharField(max_length=25)
    img = models.ImageField(upload_to='chef_photos')
    job = models.CharField(max_length=25)
    about_chef = models.CharField(max_length=255)

class Coment (models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)