from django.urls import path
from . import views

urlpatterns = [
	path ('',views.home),
	path('collaborateur',views.home_collaborateur),
	path('visiteur',views.home_visiteur),
	path('entreprise',views.home_entreprise),
	path('client',views.home_client),
]