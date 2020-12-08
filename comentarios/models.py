from django.db import models

from publicaciones.models import Publicacion


class Comentario(models.Model):
    text_commentary = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentario')

    def __str__(self):
        return self.text_commentary
