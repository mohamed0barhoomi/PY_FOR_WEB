import uuid

from django.db import models

from EntreprisesApp.models import Entreprise, TimeStampedModel


class Expedition(TimeStampedModel):
    class Statut(models.TextChoices):
        PUBLIEE = "publiee", "Publiée"
        ATTRIBUEE = "attribuee", "Attribuée"
        EN_COURS = "en_cours", "En cours"
        LIVREE = "livree", "Livrée"
        ANNULEE = "annulee", "Annulée"

    reference = models.CharField(max_length=20, unique=True, editable=False)
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    poids_kg = models.DecimalField(max_digits=10, decimal_places=2)
    date_souhaitee = models.DateField()
    description = models.TextField(blank=True)
    statut = models.CharField(
        max_length=20, choices=Statut.choices, default=Statut.PUBLIEE
    )
    entreprise = models.ForeignKey(
        Entreprise,
        on_delete=models.CASCADE,
        related_name="expeditions",
        limit_choices_to={"type_entreprise": Entreprise.TypeEntreprise.CHARGEUR},
    )

    def _generate_reference(self):
        while True:
            candidate = "EXP-" + uuid.uuid4().hex[:10].upper()
            if not Expedition.objects.filter(reference=candidate).exists():
                return candidate

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self._generate_reference()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference} : {self.ville_depart} → {self.ville_arrivee}"
