from django.db import models
from .Timespamted import TimespamtedModel

class DevinciClimbingContest(TimespamtedModel):
    active = models.BooleanField(blank=False, null=False)
    date = models.DateField(blank=True, null=True)
    titre = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.titre

    def has_change_permission(self, request, obj=None):
        return False
    
class Inscription(models.Model):
    nom = models.CharField(max_length=100, blank=False, null=False)
    prenom = models.CharField(max_length=100, blank=False, null=False)
    ecole = models.CharField(max_length=100, blank=False, null=False)
    tshirt = models.CharField(max_length=200, blank=False, null=False)
    question = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.nom