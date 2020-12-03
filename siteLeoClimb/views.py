from django.shortcuts import render, redirect

#Fonction qui redirige vers la page "Accueil"
def home_redirect(request):
	return redirect('/')

# # HTTP Error 400
# def bad_request(request, *args, **argv):
#     response = render(request,'C:/Users/samyb/Desktop/venv/siteLeoClimb/appLeoClimb/templates/400.html', status=400)
#     return response

# # HTTP Error 403
# def permission_denied(request, *args, **argv):
#     response = render(request,'C:/Users/samyb/Desktop/venv/siteLeoClimb/appLeoClimb/templates/403.html', status=403)
#     return response

# # HTTP Error 404
# def page_not_found(request, *args, **argv):
# 	response = render(request,'C:/Users/samyb/Desktop/venv/siteLeoClimb/appLeoClimb/templates/404.html', status=404)
# 	return response

# HTTP Error 500
def server_error(request, *args, **argv):
	response = render(request,'C:/Users/samyb/Desktop/venv/siteLeoClimb/appLeoClimb/templates/500.html', status=500)
	return response