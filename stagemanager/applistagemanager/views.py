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
    if not request.user.is_authenticated :
        return render(
            request,
            'applistagemanager/accueil.html'
        )
    if request.user.is_superuser : 
        lesOffres = OffreStage.objects.all()
    elif request.user.is_staff : 
        lesOffres = OffreStage.objects.filter(etat='attente')
    else :
        lesOffres = OffreStage.objects.filter(etat='validee')

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

def search(request):
    query = request.GET.get('q') 
    
    if query:
        lesOffres = OffreStage.objects.filter(intitule__icontains=query)
    else:
        lesOffres = OffreStage.objects.none()

    return render(
        request,
        'applistagemanager/offres.html',
        {'offres': lesOffres},
    )

def valider (request, id) :
    offre = OffreStage.objects.get(id_offre = id)
    offre.etat = 'validee'
    offre.save()
    return render(
        request,
        'applistagemanager/traitementValidationOffre.html',
        {'offre' : offre}
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

def formulaireModificationOffre(request, id):
    offre = OffreStage.objects.get(id_offre = id)
    form = OffreForm(instance=offre)
    return render(
        request,
        'applistagemanager/formulaireModificationOffre.html',
        {'form' : form, 'offre' : offre},
    )

def traitementFormulaireModificationOffre(request, id) :
    offre = OffreStage.objects.get(id_offre = id)

    form = OffreForm(request.POST, request.FILES, instance = offre)

    if form.is_valid():
        form.save()
    
    updatedOffre = OffreStage.objects.get(id_offre = id)

    return render(
        request,
        'applistagemanager/traitementFormulaireModificationOffre.html',
        {'intitule' : updatedOffre.intitule}
    )


def supprimerOffre(request, id):
    offre = OffreStage.objects.get(id_offre = id)
    offre.delete()
    lesOffres = OffreStage.objects.all()

    return render (
        request,
        'applistagemanager/offres.html',
        {'offres': lesOffres},
    )