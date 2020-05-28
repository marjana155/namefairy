from django.db import models

# Create your models here.


class Name(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey('names.Category', on_delete=models.CASCADE)
    gender = models.ForeignKey('names.Gender', on_delete=models.CASCADE)


class Category(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Gender(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
