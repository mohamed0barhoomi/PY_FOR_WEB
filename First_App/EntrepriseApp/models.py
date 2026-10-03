from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class utilisateur(AbstractUser):
    user_id=models.CharField(max_length=8,primary_key=True)
    email=models.EmailField(unique=True)
    role=models.CharField(max_length=20,
                          choices=[("char","chargeur"),("trans","Transporteur"),("admin","admin")],
                          default="chargeur")
    telephone=models.CharField(max_length=15,unique=True,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)




class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=200,
                                      null=False,blank=False)
    matricule_fiscale=models.CharField(max_length=17,
                                       unique=True)
    type_entrprise=models.CharField(max_length=100,
                                    choices=[("Trans","transpoteur"),("Char","chargeur")],
                                    default="chargeur"
                                    )
    addresse=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    gerant=models.OneToOneField(utilisateur,
                                on_delete=models.CASCADE,
                                related_name="Entreprise")
    


