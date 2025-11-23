from django.shortcuts import render
from applistagemanager.models import OffreStage, Candidature
from applistagemanager.forms import OffreForm
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

def Offre (request, id):
    uneOffre = OffreStage.objects.get(id_offre = id)

    return render(
        request,
        'applistagemanager/offre.html',
        {'offre' : uneOffre}
    )

def formulaireCreationOffre(request):
    form = OffreForm()

    return render(
        request,
        'applistagemanager/formulaireCreationOffre.html', 
        {'form' : form}
    )

def CreerOffre(request):
    form = OffreForm(request.POST, request.FILES)

    if form.is_valid() :
        nomOffre = form.cleaned_data['intitule']
        form.save()
    
    return render(
        request,
        'applistagemanager/traitementFormulaireCreationOffre.html',
        {'nom' : nomOffre}
    )
