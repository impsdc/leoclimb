from django.shortcuts import render, redirect

#Fonction qui redirige vers la page "Accueil"
def home_redirect(request):
	return redirect('/')

 # HTTP Error 400
def bad_request(request, *args, **argv):
	return redirect('/')

 # HTTP Error 403
def permission_denied(request, *args, **argv):
    return redirect('/')

 # HTTP Error 404
def page_not_found(request, *args, **argv):
 	return redirect('/')

# HTTP Error 500
def server_error(request, *args, **argv):
	return redirect('/')