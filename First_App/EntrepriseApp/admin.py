from django.contrib import admin
from .models import Utilisateur , Entreprise
from django.contrib.auth.admin import UserAdmin
# Register your models here.\
from .models import Entreprise , Utilisateur
from VehiculeApp.models import Vehicule





admin.site.site_header= "Mohamed Transconnect"
admin.site.site_title= "Mohamed Transconnect"
admin.site.index_title = "Tableau de bord"

class VehiculeInligne(admin.TabularInline):
    model=Vehicule
    fields=('immatriculation','type_vehicule','capacite_kg','disponible')
    extra=2
    show_change_link=True
class AdminEntreprise(admin.ModelAdmin):
    inlines=[VehiculeInligne]
    list_display=('matricule_fiscal','raison_sociale','type_entreprise','gerant')
    list_filter=('type_entreprise',"created_at","updated_at")
    search_fields=('raison_sociale',)
    list_editable=('raison_sociale',)
    #list_per_page
    #readonly_fields
    #fieldsets

class adminUSer(UserAdmin):
    list_display=("email","role",'telephone')


admin.site.register(Entreprise,AdminEntreprise)
admin.site.register(Utilisateur,adminUSer)