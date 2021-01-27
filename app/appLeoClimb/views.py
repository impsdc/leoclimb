from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages

from .models import Accueil
from .models import Post
from .models import Bureau
from .models import Promo
from .models import Palmare
from .models import Membre
from .models import Partenaire
from .models import Inscription
from .models import Galerie
from .models import Merchandising
from .models import DevinciClimbingContest


#Home
def home(request):
	obj = Partenaire.objects.all().order_by('nom')
	accueil = Accueil.objects.get()

	return render(request, 'home.html', {'obj':obj, 'accueil':accueil})

#dcc
def dcc(request):
	obj = Galerie.objects.get(id=7)
	return render(request, 'dcc.html', {'obj':obj})

#galerie
def galerie(request):
	obj = Galerie.objects.all().reverse()
	return render(request, 'galerie.html', {'obj':obj[::-1]})


#evenement
def evenement(request, titre):
	obj = Galerie.objects.get(titre=titre)
	return render(request, 'single-evenement.html', {'obj':obj})

#menbres
def menbre(request):
	obj = Bureau.objects.all().order_by('place')
	promo = Promo.objects.all()

	return render(request, 'menbres.html', {'obj':obj, 'promo': promo})

#palmares
def palmares(request):
	palmares = Palmare.objects.all()

	return render(request, 'palmares.html', {'obj': palmares})

#actualite
def actu(request):
	obj = Post.objects.all().order_by('date').reverse()

	return render(request, 'actualite.html', {'obj': obj})

#inscripiton
def inscription(request):	
	obj = DevinciClimbingContest.objects.get()

	return render(request, 'inscription.html', {'obj': obj})

#create inscription
def createInscription(request):
	if request.method == "POST":
		nom = request.POST['nom']
		prenom = request.POST['prenom']
		ecole = request.POST['ecole']
		tshirt = request.POST['tshirt']
		question = request.POST['question']

		tshirt_list = ("S", "M", "XL")
		question_list = ("Reseaux", "Asso de votre école", "Entourage", "Autres")
		
		if tshirt in tshirt_list and question in question_list:
	
			Inscription.objects.create(
				nom = nom,
				prenom = prenom,
				ecole  = ecole ,
				tshirt = tshirt ,
				question = question
			)
			messages.error(request, 'Veuillier choisir une des valeurs proposées')
			return render(request, 'inscription.html')
		else:
			messages.success(request, 'Le formulaire a bien été envoyé')
			return render(request, 'inscription.html')
	else: 
		messages.success(request, 'Le formulaire a bien été envoyé')
		return redirect("/Bureau")

#mentions
def mentions(request):
	return render(request, 'mentions.html')

#merchandising
def merchandising(request):
	obj = Merchandising.objects.all().reverse()
	return render(request, 'merchandising.html', {'obj': obj[::-1]})