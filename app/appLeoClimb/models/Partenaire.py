from django.db import models
from .Timespamted import TimespamtedModel

class Partenaire(TimespamtedModel):
    nom = models.CharField(max_length=50, blank=False, null=True)
    description = models.TextField(max_length=255, blank=False, null=False)
    logo = models.FileField(upload_to="partenaires/", blank=True, null=True)

    def __str__(self):
        return self.nom