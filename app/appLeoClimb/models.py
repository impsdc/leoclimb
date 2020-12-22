from django.contrib import admin
from django.db import models
class TimespamtedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Post(TimespamtedModel):
    title = models.CharField(max_length=100, blank=False, null=False)
    main = models.TextField(max_length=255, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    image = models.FileField(upload_to="actualite/", blank=True, null=True )

    def __str__(self):
        return self.title

admin.site.register(Post)