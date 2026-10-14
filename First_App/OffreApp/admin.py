from django.contrib import admin
from .models import Offre
# Register your models here.

class adminOffre(admin.ModelAdmin):
    list_display=('prix','statut','delai_jours','date_proposition','entreprise',"vehicule")
    list_editable=('statut',)
    search_fields=('prix',)
    list_filter=('prix','prix')
    ordering=('prix',)


admin.site.register(Offre,adminOffre)
