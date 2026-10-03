from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Utilisateur(AbstractUser):
   user_id=models.CharField(max_length=8,primary_key=True)
   email=models.EmailField(unique=True)  #string «unique»
   role = models.CharField(
    max_length=20,
    choices=[
        ("chargeur", "Chargeur"),
        ("transporteur", "Transporteur"),
        ("admin", "Admin"),
    ],
    default="chargeur",
    ) #choice
   telephone=models.CharField(max_length=8) # string
   created_at=models.DateTimeField(auto_now_add=True) # datetime
   updated_at=models.DateTimeField(auto_now=True) #datetime

class Entreprise(models.Model):
    raison_sociale=models.CharField() 
    matricule_fiscal=models.CharField(max_length=17,unique=True)# char[17] «unique»
    type_entreprise=models.CharField(choices=[("chargeur","chargeur"),
                                              ("transporteur","transporteur")]) #choice
    adresse=models.TextField()# text
    created_at=models.DateTimeField(auto_now_add=True)# datetime
    updated_at=models.DateTimeField(auto_now=True)# datetime
    gerant=models.OneToOneField(Utilisateur,
                              on_delete=models.CASCADE,
                              related_name="entrprise")