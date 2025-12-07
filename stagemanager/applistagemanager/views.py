from django.shortcuts import render, redirect
from applistagemanager.models import OffreStage, Candidature
from applistagemanager.forms import OffreForm
from applicompte.models import Etudiant
# Create your views here.

def Accueil (request):
    if not request.user.is_authenticated :
        return render(
            request,
            'applistagemanager/accueil.html',
        )
    else :
        return redirect('/offres/')

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
        {'offres': lesOffres, 'user' : request.user},
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
    if request.user.is_staff : 
        offre = OffreStage.objects.get(id_offre = id)
        offre.etat = 'validee'
        offre.save()
        return render(
            request,
            'applistagemanager/traitementValidationOffre.html',
            {'offre' : offre}
        )
    else : 
        return render('/offres/')

def refuser (request, id) : 
    if request.user.is_staff : 
        offre = OffreStage.objects.get(id_offre = id)
        offre.etat = 'refusee'
        offre.save()
        return render(
            request,
            'applistagemanager/traitementRefusOffre.html',
            {'offre' : offre}
        )
    else : 
        return render('/offres/')

def formulaireCreationOffre(request):
    if request.user.is_superuser or not request.user.is_authenticated : 
        form = OffreForm()

        return render(
            request,
            'applistagemanager/formulaireCreationOffre.html', 
            {'form' : form}
        )
    else : 
        return render('/offres/')

def CreerOffre(request):
    if request.user.is_superuser or not request.user.is_authenticated : 
        form = OffreForm(request.POST, request.FILES)

        if form.is_valid() :
            intitule = form.cleaned_data['intitule']
            form.save()
        
            return render(
                request,
                'applistagemanager/traitementFormulaireCreationOffre.html',
                {'intitule' : intitule}
            )
        else : 
            return render(
                request,
                'applistagemanager/formulaireCreationOffre.html', 
                {'form' : form} 
            )
        
    else : 
        return render('/offres/')

def formulaireModificationOffre(request, id):
    if request.user.is_superuser : 
        offre = OffreStage.objects.get(id_offre = id)
        form = OffreForm(instance=offre)
        return render(
            request,
            'applistagemanager/formulaireModificationOffre.html',
            {'form' : form, 'offre' : offre},
        )
    else : 
        return render('/offres/')

def traitementFormulaireModificationOffre(request, id) :
    if request.user.is_superuser : 
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
    else :
        return redirect('/offres/')

def supprimerOffre(request, id):
    offre = OffreStage.objects.get(id_offre = id)
    offre.delete()
    lesOffres = OffreStage.objects.all()

    return render (
        request,
        'applistagemanager/offres.html',
        {'offres': lesOffres},
    )
 
def candidater(request, id) : 
    offre = OffreStage.objects.get(id_offre = id)
    etudiant = Etudiant.objects.get(id = request.user.id)

    a_candidate = Candidature.objects.filter(etudiant = etudiant, offre = offre).exists()
    

    if a_candidate : 
        return render(
            request,
            'applistagemanager/CandidatureExisteDeja.html'
        )

    if request.user.is_authenticated : 
        if not (request.user.is_staff and request.user.is_superuser) :
            candidature = Candidature(etudiant = etudiant , offre = offre)
            candidature.save()

    
    # Verifier le nombres de candidatures
    Candidatures = Candidature.objects.filter(offre = offre)
    if len(Candidatures) >= 5 : 
        offre.etat = "cloturee"
        offre.save()

    return render(
        request,
        'applistagemanager/traitementCandidature.html',
    )

def dashboard(request) :
    if request.user.is_superuser : 
        total_offres = OffreStage.objects.count()
        offres_attentes = OffreStage.objects.filter(etat = 'attente').count()
        offres_validees = OffreStage.objects.filter(etat = 'validee').count()
        offres_refusees = OffreStage.objects.filter(etat = 'refusee').count()
        offres_cloturees = OffreStage.objects.filter(etat = 'cloturee').count()

        total_candidatures = Candidature.objects.count()

        context = {
            'total_offres' : total_offres,
            'offres_attentes' : offres_attentes,
            'offres_validees' : offres_validees,
            'offres_refusees' : offres_refusees,
            'offres_cloturees' : offres_cloturees,
            'total_candidatures' : total_candidatures, 
        }

        return render (
            request,
            'applistagemanager/dashboard.html',
            context,
        )
    else : 
        return redirect('/offres/')