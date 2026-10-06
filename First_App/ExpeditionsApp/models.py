from django.db import models
from EntrepriseApp.models import Entreprise
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone
# Create your models here.
class Expedition(models.Model):
    reference=models.CharField(max_length=20,unique=True)# string «unique»
    ville_depart=models.CharField() #string
    ville_arrivee=models.CharField() #string
    poids_kg = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(0.001)]
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
        
    @classmethod
    def _generate_ref(cls):
        annee=timezone.now().strftime('%y')
        prefixe = f"EXP_{annee}_"
        dernier=cls.objects.filter(reference__startswith=prefixe).order_by("reference").last()
        compteur=int(dernier.reference[-5:0])+1 if dernier else 1

        if compteur > 99999:
            raise ValidationError ("limit axceeded")
        return f"{prefixe} {compteur:05d}"

    
    def save(self,*args,**kwargs):
        if not self.reference:
            self.reference = self._generate_ref()

        self.full_clean()
        super.save(*args,**kwargs)
            
    
