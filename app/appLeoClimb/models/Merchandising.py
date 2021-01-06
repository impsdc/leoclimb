from django.db import models
from .Timespamted import TimespamtedModel

class Merchandising(TimespamtedModel):
    titre = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.titre

class MerchandisingImage(models.Model):
    model = models.CharField(max_length=100, blank=False, null=False)
    titre = models.CharField(max_length=200, blank=False, null=False)
    image = models.FileField(upload_to="merchandising/", blank=True, null=True)
    merchandising = models.ForeignKey(Merchandising, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.model
