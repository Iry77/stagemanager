from django.db import models
from django.contrib.auth.models import User

##########################################################
# Commandes à faire après la modification de ce fichier:
## -> Se placer dans le 2e repertoire stagemanager
## -> python manage.py makemigrations
## -> python manage.py migrate
###########################################################

# Create your models here.
class OffreStage (models.Model) :
    # id_offre : clé primaire de chaque offre qui s'auto-incrémente
    id_offre = models.AutoField(primary_key = True)

    # organisme : attribut qui permet de reconnaitre l'organisme qui publie l'offre
    organisme = models.CharField(max_length= 50)

    # Contacts de l'entreprise
    contact_nom = models.CharField(max_length = 200)
    contact_prenom = models.CharField(max_length = 200)
    contact_mail = models.EmailField()

    # Date et heure de publication qui correspond à la création de l'offre
    date_publication = models.DateTimeField(auto_now_add = True)

    # intitule : attribut qui correspond au nom du poste
    intitule = models.CharField(max_length = 200)

    # detail : attribut qui correspond aux Détails de l'offre
    detail = models.TextField()

    # Possibles états de l'offre
    STATUT_CHOIX = [
        ('attente', 'En attente de validation'),
        ('validee', 'Validée'),
        ('refusee', 'Refusée'),
        ('cloturee', 'Clôturée'),
    ]
    # etat : attribut qui correspond à l'état de l'offre
    etat = models.CharField(max_length = 10, choices = STATUT_CHOIX, default = 'attente')

    def __str__ (self):
        return self.intitule    


# Classe candidature qui relie les offres et les étudiants
class Candidature (models.Model) :
    # IdCandidature : clé primaire de chaque candidature qui s'auto-incrémente
    id_candidature = models.AutoField(primary_key = True)

    # Les clés étrangères venant des Utilisateurs et des Offres
    etudiant = models.ForeignKey(User, on_delete = models.CASCADE)
    offre = models.ForeignKey(OffreStage, on_delete = models.CASCADE)

    def __str__ (self):
        offre = self.Offre
        etudiant = self.Etudiant
        return "L'étudiant" * etudiant.username * "a postulé pour l'offre "* offre.intitule