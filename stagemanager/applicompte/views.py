from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from applistagemanager.models import OffreStage
from applicompte.models import Etudiant
# Create your views here.

# def afficherLogin(request) : pour après sécuriser login.html
    


def connexion(request):
    usr = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username = usr, password = pwd)

    if user is not None : 
        login(request, user)
        return redirect('offres')
    else :
        return render(
            request,
            'applicompte/login.html'
        )

def deconnexion(request):
    logout(request)
    return render(
        request,
        'applicompte/logout.html'
    )
