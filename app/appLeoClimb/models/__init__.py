from django.contrib import admin
from django.db import models
from .Actualite import Post
from .Bureau import Bureau, Promo
from .Palmares import Palmare, Membre
from .Partenaire import Partenaire
from .devinciclimbingcontest import DevinciClimbingContest, Inscription
from .Galerie import Galerie, GalerieImage
from .Merchandising import Merchandising, MerchandisingImage

admin.site.register(Post)
admin.site.register(Bureau)
admin.site.register(Promo)
admin.site.register(Palmare)
admin.site.register(Membre)
admin.site.register(Partenaire)
admin.site.register(DevinciClimbingContest)
admin.site.register(Inscription)
admin.site.register(Galerie)
admin.site.register(GalerieImage)
admin.site.register(Merchandising)
admin.site.register(MerchandisingImage)