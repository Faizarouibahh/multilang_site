# main/models.py

from django.db import models
from django.utils.translation import gettext_lazy as _

class Language(models.Model):
    name = models.CharField(_("Language"), max_length=50, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title

   