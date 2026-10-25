from django.contrib import admin
from .models import Expedition
# Register your models here.

class EnRetardfilter(admin.SimpleListFilter):
    title = 'En retard'
    parameter_name = 'en_retard'

    def lookups(self, request, model_admin):
        return (
            ('oui', 'Oui'),
            ('non', 'Non'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'oui':
            return queryset.filter(date_souhaitee__lt=timezone.now())
        elif self.value() == 'non':
            return queryset.filter(date_souhaitee__gte=timezone.now())
class adminExpedition(admin.ModelAdmin):
    list_display=('reference',"ville_depart","ville_arrivee","poids_kg","date_souhaitee","statut")
    list_filter=('ville_depart',"ville_arrivee","poids_kg",EnRetardfilter)
    search_fields=("poids_kg",)
    list_editable=('statut',)

admin.site.register(Expedition,adminExpedition)