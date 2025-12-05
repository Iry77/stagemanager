from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from applicompte.models import Etudiant

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Votre nom d'utilisateur",
            'id': 'floatingInput'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Votre mot de passe',
            'id': 'floatingPassword'
        })



class EtudiantUpdateForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['username', 'first_name', 'last_name', 'email', 'image']
        labels = {
            'username': "Nom d'utilisateur",
            'first_name': "Prénom",
            'last_name': "Nom",
            'email': "Adresse Email",
            'image': "Photo de profil"
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}), 
        }