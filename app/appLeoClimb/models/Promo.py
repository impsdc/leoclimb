from django.db import models
from .Timespamted import TimespamtedModel

# Create your models here.
class Promo(TimespamtedModel):
    annee = models.CharField(max_length=200, blank=False, null=False)
    image = models.FileField(upload_to="promo/", blank=True, null=True )

    def __str__(self):
        return self.annee
