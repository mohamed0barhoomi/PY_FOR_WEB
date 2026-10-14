from django.contrib import admin
from .models import Vehicule
# Register your models here.
class adminVehicule(admin.ModelAdmin):
    list_filter=('disponible',"type_vehicule")
    list_display=('immatriculation','type_vehicule','capacite_kg','disponible')
    search_fields=('type_vehicule',)
    list_editable=('disponible',)
    ordering=('disponible','capacite_kg')

admin.site.register(Vehicule,adminVehicule)