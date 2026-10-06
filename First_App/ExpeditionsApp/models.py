from django.db import models
from EntrepriseApp.models import Entreprise
from django.core.exceptions import ValidationError
# Create your models here.
class Expedition(models.Model):
    reference=models.CharField(max_length=20,unique=True)# string «unique»
    ville_depart=models.CharField() #string
    ville_arrivee=models.CharField() #string
    poids_kg = models.DecimalField(
    max_digits=10,
    decimal_places=2
    ) #decimal
    date_souhaitee=models.DateTimeField #date
    description=models.TextField()# text
    statut=models.CharField(max_length=30,choices=[("publiee","publiee"),
                                     (" attribuee"," attribuee"),
                                       ("en_cours","en_cours"),
                                       ("livree","livree"),
                                       ("annulee","annulee") ],
                                       default= "publiee")# choice
    created_at=models.DateTimeField(auto_now_add=True)# datetime
    updated_at=models.DateTimeField(auto_now=True)# datetime
    entrprise=models.ForeignKey(Entreprise,
                                   on_delete=models.CASCADE,
                                   related_name="expedition")

    def clean(self):
        super().clean()
        if self.entrprise_id and self.entrprise.type_entreprise != "chargeur" :
            raise ValidationError({
                "entreprise":"ne peut etre cree que par une entreprise de type chargeur"
            })
    
