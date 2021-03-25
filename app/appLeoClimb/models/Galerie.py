from django.db import models
from .Timespamted import TimespamtedModel

class Galerie(TimespamtedModel):
    titre = models.CharField(max_length=100, blank=False, null=False)
    ordre = models.FloatField(blank=False, null=True, unique=True)


    def __str__(self):
        return self.titre

class GalerieImage(models.Model):
    image = models.FileField(upload_to="galerie/", blank=True, null=True)
    Galerie = models.ForeignKey(Galerie, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Galerie.titre