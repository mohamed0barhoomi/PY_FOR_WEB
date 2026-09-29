from django.db import models
from vehiculeApp.models import Vehicule
from ExpertionApp.models import Expertion
# Create your models here.


class OffreApp(models.Model):
    prix = models.DecimalField(
    max_digits=10,
    decimal_places=2
)
    delai=models.IntegerField()
    status=models.CharField(choices=[])
    date_proposition=models.DateField()

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True) 

    vehicule_id=models.ForeignKey(Vehicule,
                                  on_delete=models.CASCADE,
                                  related_name="vehicules")
    expertion_id=models.ForeignKey(Expertion,
                                   on_delete=models.CASCADE,
                                   related_name="expertions")