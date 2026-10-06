from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.

matrcule_fiscalee=RegexValidator(regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$',
                                 message="format incorrect ,ex(12345678AAM000)")



def validation_email(value):
    if not value:
        raise ValidationError("laddresse email est obligatoire ")
    if not value.endswith("@gmail.com"):
        raise ValidationError("laddr must be email ")





class Utilisateur(AbstractUser):
   user_id=models.CharField(max_length=8,primary_key=True)
   email=models.EmailField(unique=True,validators=[validation_email])  #string «unique»
   role = models.CharField(
    max_length=20,
    choices=[
        ("chargeur", "Chargeur"),
        ("transporteur", "Transporteur"),
        ("admin", "Admin"),
    ],
    default="chargeur",
    ) #choice
   telephone=models.CharField(max_length=8) # string
   created_at=models.DateTimeField(auto_now_add=True) # datetime
   updated_at=models.DateTimeField(auto_now=True) #datetime

   @classmethod
   def _generateID(cls):
       annee=timezone.now().strftime("%y")
       pref=f"{annee}USER"
       dernier=cls.objects.filter(user_id__startswith=pref).order_by("user_id").last()
       compteur=int(dernier.reference[-2:0])+1 if dernier else 1

       if compteur >99:
           raise ValidationError ("limit axceeded")
       return f"{prefixe} {compteur:02d}"

   def save(self,*args,**kwargs):
           if not self.user_id:
               self.user_id = self._generateID()
   
           self.full_clean()
           super.save(*args,**kwargs)

       

class Entreprise(models.Model):
    raison_sociale=models.CharField() 
    matricule_fiscal=models.CharField(max_length=17,unique=True,validators=[matrcule_fiscalee])# char[17] «unique»
    type_entreprise=models.CharField(choices=[("chargeur","chargeur"),
                                              ("transporteur","transporteur")]) #choice
    adresse=models.TextField(validators=[
         MinLengthValidator(20,"lenght doit sup 20"),
         MaxLengthValidator(300,"laddr doit inf 300")
    ])# text
    created_at=models.DateTimeField(auto_now_add=True)# datetime
    updated_at=models.DateTimeField(auto_now=True)# datetime
    gerant=models.OneToOneField(Utilisateur,
                              on_delete=models.CASCADE,
                              related_name="entrprise")