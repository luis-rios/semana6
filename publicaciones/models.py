from django.db import models

from tags.models import Tag


class Publicacion(models.Model):
    user = models.CharField(max_length=50)
    publication_date = models.DateTimeField()
    text_publication = models.CharField(max_length=200)

    tag = models.ManyToManyField(Tag, related_name='publicacion')

    def __str__(self):
        return self.user
