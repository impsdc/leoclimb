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

    url(r'^Notre-association/$', views.association), #url relié à notre fonction "home"
    url(r'^Le-bureau/$', views.page_le_bureau), #url relié à notre fonction "page_le_bureau"
    url(r'^Collections-LeoClimb/$', views.page_collection), #url relié à notre fonction "page_collection"
    url(r'^Actualites/$', views.page_news), #url relié à notre fonction "page_news"
    url(r'^Devinci-climbing-contest/$', views.page_dcc), #url relié à notre fonction "page_partenaire"
    url(r'^Evenements/Shooting-2019/$', views.page_evenements_shooting2019), #url relié à notre fonction "page_evenements_shooting2019"
    url(r'^Evenements/Contest-Blocbuster-2019/$', views.page_evenements_contestBB2019), #url relié à notre fonction "page_evenements_contestBB2019"
    url(r'^Evenements/WEI-2019/$', views.page_evenements_WEI2019), #url relié à notre fonction "page_evenements_WEI2019"
    url(r'^Evenements/Remise-Collection-2019/$', views.page_evenements_remise2019), #url relié à notre fonction "page_evenements_remise2019"
    url(r'^Evenements/LeoClimb-Etranger-2019/$', views.page_evenements_leoclimbEtranger2019),
    url(r'^Evenements/Murmur-2019/$', views.page_evenements_murmur2019), #url relié à notre fonction "page_evenements_murmur2019"
    url(r'^Evenements/DCC-2019/$', views.page_evenements_DCC2019), #url relié à notre fonction "page_evenements_DCC2019"
    url(r'^DCC/$', views.page_evenements_DCC), #url relié à notre fonction "page_evenements_DCC"
    url(r'^Evenements/JPO-2020/$', views.page_evenements_jpo2020), #url relié à notre fonction "page_evenements_jpo2020"
    url(r'^Evenements/Murmur-2020/$', views.page_evenements_murmur2020), #url relié à notre fonction "page_evenements_murmur2020"
]