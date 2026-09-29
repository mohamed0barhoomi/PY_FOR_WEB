from django.db import models
from EntrepriseApp.models import Entreprise

# Create your models here.


class Vehicule (models.Model):
    immatriculation=models.CharField(unique=True,max_length=100)
    type_vehicule=models.CharField(max_length=20,choices=[("camionnette","amionnette"),("fourgon", "fourgon"), ("ca_pot","camion porteur"),("sem_remr", "semi-remorque")])
    capacite_kg=models.IntegerField()
    dsiponible=models.BooleanField()

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)    

    entreprise_id=models.ForeignKey(Entreprise,
                                      on_delete=models.CASCADE,
                                      related_name="vehicules")
