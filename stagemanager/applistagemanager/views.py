from django.shortcuts import render
from applistagemanager.models import OffreStage, Candidature

# Create your views here.
def Offres (request):
    lesOffres = OffreStage.objects.all()

    return render (
        request, 
        'applistagemanager/offres.html',
        {'offres': lesOffres},
    )