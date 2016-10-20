from django.db import models

# Create your models here.
class Deneme(models.Model):
    title=models.CharField(max_length=50)
    ad=models.CharField(max_length=50)
    soyad=models.CharField(max_length=50)
    def __str__(self):
        return self.title