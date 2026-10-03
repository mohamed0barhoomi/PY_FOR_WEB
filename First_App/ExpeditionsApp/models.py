from django.db import models
from EntrepriseApp.models import Entreprise
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
    entrprise_id=models.ForeignKey(Entreprise,
                                   on_delete=models.CASCADE,
                                   related_name="expedition")
