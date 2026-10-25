from django.contrib import admin
from .models import Offre
# Register your models here.


import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Offre


@admin.action(description="Exporter la sélection en CSV")
def exporter_offres_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="offres.csv"'

    # Permet à Excel de reconnaître correctement les caractères accentués
    response.write('\ufeff')

    writer = csv.writer(response)

    # En-têtes du fichier CSV
    writer.writerow([
        'reference_expedition',
        'entreprise',
        'prix',
        'statut',
        'delai_jours',
        'date_proposition'
    ])

    # Précharger les objets liés pour limiter les requêtes SQL
    offres = queryset.select_related('expedition', 'entreprise')

    for offre in offres:
        writer.writerow([
            offre.expedition.reference,
            offre.entreprise,
            offre.prix,
            offre.statut,
            offre.delai_jours,
            offre.date_proposition
        ])

    return response


class adminOffre(admin.ModelAdmin):
    list_display=('prix','statut','delai_jours','date_proposition','entreprise')
    list_editable=('statut',)
    search_fields=('prix',)
    list_filter=('prix','prix')
    ordering=('prix',)
    actions=[exporter_offres_csv]


admin.site.register(Offre,adminOffre)
