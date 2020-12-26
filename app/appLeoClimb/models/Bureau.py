from django.db import models
from .Timespamted import TimespamtedModel

# Create your models here.
class Bureau(TimespamtedModel):
    poste = models.CharField(max_length=20, blank=False, null=False)
    nom = models.CharField(max_length=100, blank=False, null=False)
    citation = models.CharField(max_length=160, blank=False, null=False)
    image = models.FileField(upload_to="bureau/", blank=True, null=True )

    def __str__(self):
        return self.nom
