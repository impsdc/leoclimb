from django.shortcuts import render, redirect
from django.template import RequestContext

from .models import Post
from .models import Bureau
from .models import Palmare
from .models import Membre
from .models import Partenaire
from .models import Inscription


#Home
def home(request):
	obj = Partenaire.objects.all()

	return render(request, 'home.html', {'obj':obj})

#dcc
def dcc(request):
	return render(request, 'dcc.html')

#galerie
def galerie(request):
	return render(request, 'galerie.html')

#menbres
def menbre(request):
	obj = Bureau.objects.all()

	return render(request, 'menbres.html', {'obj':obj})

#palmares
def palmares(request):
	palmares = Palmare.objects.all()

	return render(request, 'palmares.html', {'obj': palmares})

#actualite
def actu(request):
	obj = Post.objects.all().order_by('date').reverse()
	
	return render(request, 'actualite.html', {'obj': obj})

#merchandising
def inscription(request):
	return render(request, 'inscription.html')

#create inscription
def createInscription(request):
	if request.method == "POST":
		nom = request.POST['nom']
		prenom = request.POST['prenom']
		ecole = request.POST['ecole']
		tshirt = request.POST['tshirt']
		question = request.POST['question']

		
		Inscription.objects.create(
			nom = nom,
			prenom = prenom,
			ecole  = ecole ,
			tshirt = tshirt ,
			question = question
		)

		return redirect("/")
	else: 
		return redirect("/Bureau")

#mentions
def mentions(request):
	return render(request, 'mentions.html')

#merchandising
def merchandising(request):
	return render(request, 'merchandising.html')


#Fonction qui dirige vers la page "L'association" du site.
def association(request):
	return render(request, 'association.html')

#Fonction qui dirige vers la page "Le bureau" du site.
def page_le_bureau(request):
	return render(request, 'bureau.html')

#Fonction qui dirige vers la page "Collections" du site.
def page_collection(request):
	return render(request, 'vetements.html')

#Fonction qui dirige vers la page "News" du site.
def page_news(request):
	return render(request, 'news.html')

#Fonction qui dirige vers la page "Partenaires" du site.
def page_dcc(request):
	return render(request, 'dcc.html')

#Fonction qui dirige vers la page "Evenements" du site.
def page_evenements(request):
	return render(request, 'evenements.html')

#Fonction qui dirige vers la page "Shooting" du site.
def page_evenements_shooting2019(request):
	return render(request, 'evenements/shooting2019.html')

#Fonction qui dirige vers la page "Remise 2019" du site.
def page_evenements_remise2019(request):
	return render(request, 'evenements/remise2019.html')

#Fonction qui dirige vers la page "WEI 2019" du site.
def page_evenements_WEI2019(request):
	return render(request, 'evenements/WEI2019.html')

#Fonction qui dirige vers la page "Murmur 2019" du site.
def page_evenements_murmur2019(request):
	return render(request, 'evenements/murmurIssy2019.html')

#Fonction qui dirige vers la page "A l'étranger" du site.
def page_evenements_leoclimbEtranger2019(request):
	return render(request, 'evenements/leoclimbEtranger2019.html')

#Fonction qui dirige vers la page "Nous soutenir" du site.
def page_evenements_contestBB2019(request):
	return render(request, 'evenements/contestBB2019.html')

#Fonction qui dirige vers la page "DCC 2019 photo" du site.
def page_evenements_DCC2019(request):
	return render(request, 'evenements/DCC2019photo.html')

#Fonction qui dirige vers la page "DCC page" du site.
def page_evenements_DCC(request):
	return render(request, 'evenements/DCC2019page.html')

#Fonction qui dirige vers la page "JPO 2020" du site.
def page_evenements_jpo2020(request):
	return render(request, 'evenements/jpo2020.html')

#Fonction qui dirige vers la page "Murmur 2020" du site.
def page_evenements_murmur2020(request):
	return render(request, 'evenements/murmurIssy2020.html')
