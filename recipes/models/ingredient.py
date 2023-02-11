from django.db import models


class Ingredient(models.Model):
    name_singular = models.CharField(max_length=200, null=True, blank=True, default='')
    name_plural = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return f"{self.name_singular} ({self.name_plural})"
