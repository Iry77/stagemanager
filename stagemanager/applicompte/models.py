from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Etudiant(User):
    image = models.ImageField(default= '/imagesEtudiant/default.png', upload_to="imageEtudiant")