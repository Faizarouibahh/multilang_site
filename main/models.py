# main/models.py

from django.db import models
from django.utils.translation import gettext_lazy as _

class Language(models.Model):
    name = models.CharField(_("Language"), max_length=50, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    content = models.TextField(_("Content"))
    publication_date = models.DateTimeField(_("Publication Date"), auto_now_add=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name=_("Language"), default=1)  # Utiliser une valeur par défaut


    def __str__(self):
        return self.title