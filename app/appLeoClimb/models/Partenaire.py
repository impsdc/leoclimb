from django.db import models
from .Timespamted import TimespamtedModel

class Partenaire(TimespamtedModel):
    nom = models.CharField(max_length=50, blank=False, null=True)
    description = models.TextField(blank=False, null=False)
    logo = models.FileField(upload_to="partenaires/", blank=True, null=True)
    ordre = models.FloatField(blank=False, null=True, unique=True)

    def clean(self, *args, **kwargs):
        if self.ordre:
            try:
                Partenaire.objects.filter(ordre=self.ordre).update(ordre=None)
            except Galerie.DoesNotExist:
                pass


    def __str__(self):
        return self.nom