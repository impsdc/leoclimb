from django.db import models
from .Timespamted import TimespamtedModel

# Create your models here.
class Bureau(TimespamtedModel):
    poste = models.CharField(max_length=50, blank=False, null=False)
    nom = models.CharField(max_length=100, blank=False, null=False)
    citation = models.CharField(max_length=160, blank=False, null=False)
    image = models.FileField(upload_to="bureau/", blank=True, null=True)
    insta = models.URLField(blank=True, null=True)
    place = models.FloatField(blank=False, null=False, default=0, unique=True)

    def __str__(self):
        return self.nom

class Promo(TimespamtedModel):
    annee = models.CharField(max_length=200, blank=False, null=False)
    image = models.FileField(upload_to="promo/", blank=True, null=True )

    def __str__(self):
        return self.annee
