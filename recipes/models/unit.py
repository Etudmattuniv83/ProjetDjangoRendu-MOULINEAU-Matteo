from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return self.name
