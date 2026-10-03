from django.db import models

from EntreprisesApp.models import Entreprise, TimeStampedModel


class Vehicule(TimeStampedModel):
    class TypeVehicule(models.TextChoices):
        CAMIONNETTE = "camionnette", "Camionnette"
        FOURGON = "fourgon", "Fourgon"
        CAMION_PORTEUR = "camion_porteur", "Camion porteur"
        SEMI_REMORQUE = "semi_remorque", "Semi-remorque"

    immatriculation = models.CharField(max_length=20, unique=True)
    type_vehicule = models.CharField(
        max_length=20, choices=TypeVehicule.choices
    )
    capacite_kg = models.PositiveIntegerField()
    disponibilite = models.BooleanField(default=True)
    entreprise = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        related_name="vehicules",
        limit_choices_to={"type_entreprise": Entreprise.TypeEntreprise.TRANSPORTEUR},
    )

    def __str__(self):
        return f"{self.immatriculation} ({self.get_type_vehicule_display()})"
