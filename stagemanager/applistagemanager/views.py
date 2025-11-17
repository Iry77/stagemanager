from django.shortcuts import render
from applistagemanager.models import OffreStage, Candidature

# Create your views here.

def Accueil (request):
    return render(
        request,
        'applistagemanager/accueil.html',
    )

# Méthode pour la liste des offres
def Offres (request):
    lesOffres = OffreStage.objects.all()

    return render (
        request, 
        'applistagemanager/offres.html',
        {'offres': lesOffres},
    )