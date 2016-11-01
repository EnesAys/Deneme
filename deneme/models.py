from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_text
from django.conf import settings

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

    def review_count(self):
        return self.review_set.count()

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    konu = models.ForeignKey(Konu)
    comment = models.TextField(null=True, blank=True)
    vote = models.IntegerField(
        default=3,
        choices=(
            (1, 'Berbat'),
            (2, 'Kötü'),
            (3, 'Meh'),
            (4, 'Uh'),
            (5, 'Yıkılıyor'),
        )
    )

    def __str__(self):
        return smart_text(self.comment),self.konu,self.user