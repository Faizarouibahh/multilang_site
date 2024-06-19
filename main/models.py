
from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    content = models.TextField(_("Content"))
    publication_date = models.DateTimeField(_("Publication Date"), auto_now_add=True)

    def __str__(self):
        return self.title
