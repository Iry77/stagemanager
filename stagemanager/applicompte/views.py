from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from applistagemanager.models import OffreStage
from applicompte.models import Etudiant, User
from applicompte.forms import EtudiantUpdateForm
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

def formulaireInscription(request) : 
    return render(
        request,
        'applicompte/formulaireInscription.html'
    )

def traitementFormulaireInscription(request) : # à revoir
    prenom = request.POST['first_name']
    nom = request.POST['last_name']
    usr = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    img = request.POST['image']

    user = Etudiant()
    if img :
        user.image = img

    user.first_name = prenom
    user.last_name = nom
    user.username = usr
    user.email = email
    user.set_password(password)

    user.save()

    return redirect('offres')

def formulaireProfil(request) : 
    user = None

    if request.user.is_authenticated :
        user = Etudiant.objects.get(id = request.user.id)
        form = EtudiantUpdateForm(instance= user)
        return render(
            request,
            'applicompte/formulaireProfil.html',
            {'user' : user, 'form' : form},
        )
    
    else : 
        return render (
            request,
            'applicompte/login.html',
        )

def traitementFormulaireProfil(request):
    # 1. On vérifie si connecté
    if request.user.is_authenticated:
        
        # 2. LA CLÉ EST ICI : On cible directement la sous-partie "etudiant"
        # Cela permet au formulaire d'accéder au champ "image"
        etudiant = request.user.etudiant

        if request.method == 'POST':
            # On lie le formulaire à l'étudiant (et pas juste au User)
            form = EtudiantUpdateForm(request.POST, request.FILES, instance=etudiant)
            
            if form.is_valid():
                form.save()
                return render(
                    request, 
                    'applicompte/traitementFormulaireProfil.html', 
                    {'user': request.user}
                )
        
        else:
            # Pré-remplissage avec les données de l'étudiant
            form = EtudiantUpdateForm(instance=etudiant)
            
        return render(
            request,
            'applicompte/formulaireProfil.html',
            {'form': form}
        )
    
    else:
        return redirect('/login/')
    
