from django.db import models
from EntrepriseApp.models import Entreprise
# Create your models here.
class Vehicule(models.Model):
    immatriculation=models.CharField(max_length=11,unique=True)# string «unique»
    type_vehicule=models.CharField(choices=[ ("camionnette","camionnette"),
                                             ("fourgon","fourgon"),
                                             (" camion porteur"," camion porteur"),
                                             (" semi-remorque"," semi-remorque")
                                             ]) #choice
    capacite_kg=models.IntegerField()# int
    disponible=models.BooleanField(default=True)# bool
    created_at=models.DateTimeField(auto_now_add=True)# datetime
    updated_at=models.DateTimeField(auto_now=True) #datetime
    entrprise=models.ForeignKey(Entreprise,
                                on_delete=models.CASCADE,
                                related_name="vehicule")