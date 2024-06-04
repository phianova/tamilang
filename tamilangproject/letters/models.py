from django.db import models

# Create your models here.

class Letter(models.Model):
    tamil = models.CharField(max_length=10)
    phonetic = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)
    type = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.tamil} - {self.phonetic}"

class User(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

