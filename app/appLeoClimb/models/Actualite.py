from django.db import models
from .Timespamted import TimespamtedModel

# Create your models here.
class Post(TimespamtedModel):
    title = models.CharField(max_length=100, blank=False, null=False)
    main = models.TextField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    image = models.FileField(upload_to="actualite/", blank=True, null=True )

    def __str__(self):
        return self.title
