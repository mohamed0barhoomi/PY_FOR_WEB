from django.db import models

from EntreprisesApp.models import Entreprise, TimeStampedModel
from ExpeditionsApp.models import Expedition
from VehiculesApp.models import Vehicule


class Offre(TimeStampedModel):
    class Statut(models.TextChoices):
        PROPOSEE = "proposee", "Proposée"
        ACCEPTEE = "acceptee", "Acceptée"
        REFUSEE = "refusee", "Refusée"
        RETIREE = "retiree", "Retirée"

    prix = models.DecimalField(max_digits=10, decimal_places=2)
    delai_jours = models.PositiveIntegerField()
    statut = models.CharField(
        max_length=20, choices=Statut.choices, default=Statut.PROPOSEE
    )
    date_proposition = models.DateField(auto_now_add=True)

    expedition = models.ForeignKey(
        Expedition,
        on_delete=models.CASCADE,
        related_name="offres",
    )
    transporteur = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        related_name="offres",
        limit_choices_to={"type_entreprise": Entreprise.TypeEntreprise.TRANSPORTEUR},
    )
    vehicule = models.ForeignKey(
        Vehicule,
        on_delete=models.CASCADE,
        related_name="offres",
        limit_choices_to={"disponibilite": True},
    )

    def __str__(self):
        return f"Offre {self.prix} pour {self.expedition.reference} ({self.get_statut_display()})"
