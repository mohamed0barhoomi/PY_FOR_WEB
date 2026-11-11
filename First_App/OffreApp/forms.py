from django import forms
from .models import Offre


class OffreForm(forms.ModelForm):

    class Meta:
        model = Offre
        exclude = [
            "created_at",
            "updated_at",
        ]

        widgets = {"date_proposition": forms.DateInput(attrs={"type": "date"})}
