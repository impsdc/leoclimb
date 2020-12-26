from django.db import models
from .Timespamted import TimespamtedModel

# Create your models here.
class Palmares(TimespamtedModel):
    titre = models.CharField(max_length=20, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    image = models.FileField(upload_to="palmares/", blank=True, null=True )

    def __str__(self):
        return self.titre
