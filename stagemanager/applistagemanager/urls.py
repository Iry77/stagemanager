from django.contrib import admin 
from django.urls import path
from applistagemanager import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Accueil),
    path('offres/', views.Offres, name = 'offres'),
    path('offres/search', views.search, name = 'search'),
    path('offres/<int:id>', views.Offre),
    path('offres/add', views.formulaireCreationOffre),
    path('offres/create', views.CreerOffre ),
    path('offres/<int:id>/update', views.formulaireModificationOffre),
    path('offres/<int:id>/updated', views.traitementFormulaireModificationOffre),
    path('offres/<int:id>/delete', views.supprimerOffre),
    path('offres/<int:id>/valider', views.valider),
]

urlpatterns += static(settings.MEDIA_URL, documant_root = settings.MEDIA_ROOT)