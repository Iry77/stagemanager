from django.contrib import admin 
from django.urls import path
from applicompte import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'applicompte/login.html'), name = 'login'),
    path('logout/', views.deconnexion, name ="logout"),
    path('connexion/', views.connexion),
    path('register/', views.formulaireInscription),
    path('inscription/', views.traitementFormulaireInscription),
    path('user/update/', views.formulaireProfil),
    path('user/updated/', views.traitementFormulaireProfil)


]

urlpatterns += static(settings.MEDIA_URL, documant_root = settings.MEDIA_ROOT)