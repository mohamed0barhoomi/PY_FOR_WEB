from django.contrib import admin
from .models import Expedition
# Register your models here.
class adminExpedition(admin.ModelAdmin):
    list_display=('reference',"ville_depart","ville_arrivee","poids_kg","date_souhaitee","statut")
    list_filter=('ville_depart',"ville_arrivee","poids_kg")
    search_fields=("poids_kg",)
    list_editable=('statut',)

admin.site.register(Expedition,adminExpedition)