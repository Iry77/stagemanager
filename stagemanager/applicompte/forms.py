from django import forms # <--- Import nécessaire pour accéder à forms.TextInput
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User # <--- Import correct du modèle User standard

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

class UserUpdateForm(forms.ModelForm): 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': "Nom d'utilisateur",
            'first_name': "Prénom",
            'last_name': "Nom",
            'email': "Adresse Email"
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }