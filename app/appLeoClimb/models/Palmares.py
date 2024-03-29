from django.db import models
from .Timespamted import TimespamtedModel

class Palmare(TimespamtedModel):
    titre = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    image = models.FileField(upload_to="palmares/", blank=True, null=True)
    ordre = models.FloatField(blank=False, null=True, unique=True)

    def clean(self, *args, **kwargs):
        if self.ordre:
            try:
                Palmare.objects.filter(ordre=self.ordre).update(ordre=None)
            except Galerie.DoesNotExist:
                pass

    def __str__(self):
        return self.titre

class Membre(models.Model):
    nom = models.CharField(max_length=100, blank=False, null=False)
    place = models.CharField(max_length=200, blank=False, null=False)
    menbre = models.ForeignKey(Palmare, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
