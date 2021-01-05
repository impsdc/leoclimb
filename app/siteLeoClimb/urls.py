"""siteLeoClimb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url, include
# #Importation de notre views.py
# from . import views

# urlpatterns = [
#     url(r'^$', views.home_redirect,name='home_redirect'),
#     path('Notre-association/', views.association), #url relié à notre fonction "home"
#     path('LeoClimb/', views.home), #url relié à notre fonction "home"
#     path('Contact/', views.contact), #url relié à notre fonction "contact"
#     path('Nous-soutenir/', views.nous_Soutenir), #url relié à notre fonction "nous_Soutenir"
# #    path('', views.home()), #url relié à notre fonction home
#     path('admin/', admin.site.urls),
# ]
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from siteLeoClimb import views 
from django.conf.urls import (
handler400, handler403, handler404, handler500
)
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('appLeoClimb.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler400 = 'appLeoClimb.views.bad_request'
# handler403 = 'appLeoClimb.views.permission_denied'
# handler404 = 'appLeoClimb.views.page_not_found'
handler500 = 'siteLeoClimb.views.server_error'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
