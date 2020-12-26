from django.contrib import admin
from django.db import models
from .Actualite import Post
from .Bureau import Bureau
from .Promo import Promo
from .Palmares import Palmares

admin.site.register(Post)
admin.site.register(Bureau)
admin.site.register(Promo)
admin.site.register(Palmares)