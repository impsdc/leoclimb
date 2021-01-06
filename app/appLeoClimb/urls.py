from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


#Importation de notre views.py
from . import views

urlpatterns = [
    #home
    path('', views.home, name='home'), 

    #dcc
    path('Devinci-Climbing-Contest', views.dcc, name='dcc'), 

    #galerie
    path('Galerie', views.galerie, name='galerie'), 

    #menbre
    path('Menbres', views.menbre, name='menbres'), 

    #palmares
    path('Palmares', views.palmares, name='palmares'), 

    #actualite
    path('Actualites', views.actu, name='actualites'),

    #mentions-legales
    path('Mentions-legales', views.mentions, name='mentions'), 
    
    #merchandising
    path('Merchandising', views.merchandising, name='merchandising'), 

    #dcc Inscription
    path('Devinci-Climbing-Conntest/inscription', views.inscription, name='inscription'), 
    #handle form
    path('Devinci-Climbing-Conntest/inscription/submit', views.createInscription, name='createInscription'), 

    path('Evenement/<str:titre>/', views.evenement, name="evenement"),
]