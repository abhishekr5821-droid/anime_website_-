from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    def __str__(self):
        return self.username


class Anime(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='anime/')

    def __str__(self):
        return self.title