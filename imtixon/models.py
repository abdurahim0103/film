from django.db import models

# Create your models here.

class Actor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)
    adress = models.TextField()
    birth_day = models.DateField()


class Category(models.Model):
    name = models.CharField(max_length=100)

class Film(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_created=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True, blank=True)

class Info(models.Model):
    film = models.ForeignKey(Film, on_delete = models.CASCADE, null = True, blank=True)
    actor = models.ForeignKey(Actor, on_delete = models.CASCADE, null=True, blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True, blank=True)


