from django.db import models
from .Timespamted import TimespamtedModel
from django.core.exceptions import ValidationError

# Create your models here.
class Post(TimespamtedModel):
    title = models.CharField(max_length=100, blank=False, null=False)
    main = models.TextField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    image = models.FileField(upload_to="actualite/", blank=True, null=True)
    accueil = models.BooleanField(blank=False, null=True)

    def is_available(self):
        temp = Post.objects.filter(accueil=True)
        if len(temp) >= 3:
            return False
        else:
            return True

    def clean(self):
        if not self.is_available():
            raise ValidationError('Il y a déjà 3 articles à la une')

    def __str__(self):
        return self.title
