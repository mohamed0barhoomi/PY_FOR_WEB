from django.db import models
from EntrepriseApp.models import Entreprise
from VehiculeApp.models import Vehicule
from ExpeditionsApp.models import Expedition
# Create your models here.
class Offre(models.Model):
    prix = models.DecimalField(
    max_digits=10,
    decimal_places=2
    )# decimal
    delai_jours=models.PositiveIntegerField()# int
    statut=models.CharField(choices=[ ("proposee","proposee"), 
                                     ("acceptee","acceptee"),
                                     ("refusee","refusee"),
                                     ("retiree","retiree")],
                            default="proposee")# choice
    date_proposition=models.DateField() #date
    created_at=models.DateTimeField(auto_now_add=True) # datetime
    updated_at=models.DateTimeField(auto_now=True) #datetime
    entreprise=models.ForeignKey(Entreprise,
                                 on_delete=models.CASCADE,
                                 related_name="offre")
    vehicule=models.ForeignKey(Vehicule,
                               on_delete=models.CASCADE,
                               related_name="offre")
    expedition=models.ForeignKey(Expedition,
                                 on_delete=models.CASCADE,
                                 related_name="expedition")
