from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Deneme(models.Model):
    title=models.CharField(max_length=50)
    ad=models.CharField(max_length=50)
    soyad=models.CharField(max_length=50)
    def __str__(self):
        return self.title
class Konu(models.Model):
    title=models.CharField(max_length=255,null=False)
    description=models.TextField()
    writer=models.ForeignKey(User)
    date=models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, blank=True,
                                   related_name='liked_places')
    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('konu_detail', (self.id,))
