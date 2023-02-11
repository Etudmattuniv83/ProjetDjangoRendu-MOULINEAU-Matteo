from django.db import models

from recipes.models.tag import Tag


class Articles(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, default='')
    descrption = models.CharField(max_length=200, null=True, blank=True, default='')
    prix = models.FloatField()
    thumbnail = models.ImageField(upload_to="products", blank=True)
    def __str__(self):
        return f"{self.id} - {self.title}"
