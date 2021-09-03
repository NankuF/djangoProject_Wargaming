from django.conf import settings
from django.db import models


# Create your models here.

class Table(models.Model):
    file = models.FileField(upload_to=settings.MEDIA_ROOT)
    city = models.CharField(max_length=128, blank=True, null=True)
    word_TF = models.FloatField(blank=True, null=True)
    word_IDF = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.city} |{self.word_TF}| {self.word_IDF}\n'
