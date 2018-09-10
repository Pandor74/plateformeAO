from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404

# Create your views here.

def home(request):
	connected = True
	if connected:
		collaborateur=False
		if collaborateur:
			return redirect(home_collaborateur)
		else:
			entreprise=False
			if entreprise:
				return redirect(home_entreprise)
			else:
				return redirect(home_client)
	else:
		return redirect(home_visiteur)

def home_collaborateur(request):
	
	return render(request,'plateforme/accueil_collaborateur.html',locals())

def home_visiteur(request):
	
	return render(request,'plateforme/accueil_visiteur.html',locals())	

def home_entreprise(request):
	
	return render(request,'plateforme/accueil_entreprise.html',locals())

def home_client(request):
	
	return render(request,'plateforme/accueil_client.html',locals())	