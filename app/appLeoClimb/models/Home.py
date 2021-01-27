from django.db import models
from .Timespamted import TimespamtedModel

# Create your models here.
class Accueil(TimespamtedModel):
    title = models.CharField(max_length=100, blank=False, null=False)
    subtitle = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title
