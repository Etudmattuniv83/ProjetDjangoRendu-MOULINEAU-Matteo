from django.db import models


class Tag(models.Model):
    text = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return self.text
