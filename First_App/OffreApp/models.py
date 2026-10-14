from django.db import models
from EntrepriseApp.models import Entreprise
from VehiculeApp.models import Vehicule
from ExpeditionsApp.models import Expedition
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator,MinValueValidator
from django.db import transaction
# Create your models here.
class Offre(models.Model):
    prix = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(1,"le prix doit sup a 0")]
    )# decimal
    delai_jours=models.PositiveIntegerField(validators=[MinValueValidator(1,"le delai doit sup ou egal a 1")])# int
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


    def clean(self):
            super().clean()
            if self.entreprise and self.entreprise.type_entreprise != "transporteur"  :
                raise ValidationError({
                    "entreprise":"ne peut etre cree que par une entreprise de type transporteur"
                })
            if  self.vehicule.entrprise_id != self.entreprise_id:
                 raise ValidationError({"vehicule":" must be the same of entreprise "})
            if self.entreprise and self.expedition and self.statut == "proposee":
                 offre_exisiste=Offre.objects.filter(
                      entreprise=self.entreprise,
                      expedition=self.expedition,
                      statut="proposee"
                 )
            if self.pk:
                 offre_exisiste=offre_exisiste.exclude(pk=self.pk)
            if offre_exisiste.exists():
                 raise ValidationError({
                      "offre":"cette entreprise possede deja une offre au status propose pour cette expedition"
                 })
            
            if self.vehicule and not self.vehicule.disponible:
                raise ValidationError({
                    "vehicule":"vehicule not disponible to offre"
                })
            
            if self.expedition and self.vehicule:
                if self.expedition.poids_kg < 1500 and self.vehicule.type_vehicule != "camionnette":
                    raise ValidationError({
                        "type vehicule ":" must be compatible with the expedition poids"
                    })
                if self.expedition.poids_kg >= 1500 and self.expedition.poids_kg <3500 and self.vehicule.type_vehicule != "fourgon":
                    raise ValidationError({
                        "type vehicule ":" must be compatible with the expedition poids"
                    })
                if self.expedition.poids_kg >= 3500 and self.expedition.poids_kg <19000 and self.vehicule.type_vehicule != "semi-remorque":
                    raise ValidationError({
                        "type vehicule ":" must be compatible with the expedition poids"
                    })
                if self.expedition.poids_kg >= 19000 and self.expedition.poids_kg <=26000 and self.vehicule.type_vehicule != "camion-porteur":
                    raise ValidationError({
                        "type vehicule ":" must be compatible with the expedition poids"
                    })
                
    def __str__(self):
            return self.statut            
                
                
            
    

    def save(self, *args, **kwargs):
      with transaction.atomic():

        ancien_statut = None
        if self.pk:
            ancienne_offre = Offre.objects.filter(pk=self.pk).first()
            if ancienne_offre:
                ancien_statut = ancienne_offre.statut
        super().save(*args, **kwargs)

       
        if self.statut == "acceptee" and ancien_statut != "acceptee":
            
            Expedition.objects.filter(
                pk=self.expedition_id
            ).update(statut="attribuee")

            Offre.objects.filter(
                expedition_id=self.expedition_id,
                statut="proposee"
            ).exclude(
                pk=self.pk
            ).update(statut="refusee")

    