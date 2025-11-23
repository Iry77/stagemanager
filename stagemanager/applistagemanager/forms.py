from django import forms
from django.forms import ModelForm
from applistagemanager.models import OffreStage

class OffreForm(forms.ModelForm) :
    class Meta : 
        model = OffreStage
        fields = ['organisme','logo','intitule','detail','contact_nom','contact_prenom','contact_mail']
        labels = {
            'organisme' : 'Le nom de votre entreprise',
            'logo' : 'Le logo de votre entreprise',
            'intitule' : "L'intitulé du poste",
            'detail': "Les détails du poste",
            'contact_nom': 'Le nom du responsable de cet offre',
            'contact_prenom': 'Le prénom du responsable de cet offre',
            'contact_mail' : 'Le mail du responable de cet offre'
        }