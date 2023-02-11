from django.db import models

from recipes.models.tag import Tag


class Recipe(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, default='')
    summary = models.CharField(max_length=200, null=True, blank=True, default='')
    content = models.TextField(null=True, blank=True, default='')
    tags = models.ManyToManyField(Tag, related_name='recipes')

    def __str__(self):
        return f"{self.id} - {self.title}"
