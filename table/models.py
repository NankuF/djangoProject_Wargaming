from django.db import models


class File(models.Model):
    name_file = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name_file


class Table(models.Model):
    word = models.CharField(max_length=128, blank=True, null=True)
    word_TF = models.FloatField(blank=True, null=True)
    word_IDF = models.FloatField(blank=True, null=True)
    filename = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f'{self.word} {self.filename}'


class ResultTable(models.Model):
    word = models.CharField(max_length=128, blank=True, null=True)
    word_TF = models.FloatField(blank=True, null=True)
    word_IDF = models.FloatField(blank=True, null=True)
    filename = models.CharField(max_length=128, blank=True, null=True)
