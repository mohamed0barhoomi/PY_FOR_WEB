from django.contrib import admin
from .models import Utilisateur , Entreprise
# Register your models here.
class AdminEntreprise(admin.ModelAdmin):
    list_display=('matricule_fiscal','raison_sociale','type_entreprise','gerant')
    list_filter=('type_entreprise',"created_at","updated_at")
    search_fields=('raison_sociale',)
    list_editable=('raison_sociale',)

admin.site.register(Entreprise,AdminEntreprise)
admin.site.register(Utilisateur)