from django.db import models

# Create your models here.


class Expertion(models.Model):
     reference=models.CharField(unique=True)
     ville_dep=models.CharField()
     ville_arr=models.CharField()
     poid=models.FloatField()
     date_souhaitte=models.DateField(auto_now_add=True)
     descreption=models.TextField()
     status=models.CharField(choices=[("publiee","publiee"),("attribuee","attribuee"),("en cour","en cour"),("livre","livre"),("annulee","annulee") ])
     
     create_at=models.DateTimeField(auto_now_add=True)
     update_at=models.DateTimeField(auto_now=True) 
