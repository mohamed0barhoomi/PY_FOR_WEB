from django.urls import path
from .views import (
    home, list_ent, details_ent, delete_ent,
    Entreprise_list, Entreprise_detail, Entreprise_delete, Entreprise_create, Entreprise_update,
)

app_name = "entreprise"

urlpatterns = [
    path("", home, name="home"),
    path("list/", list_ent, name="list"),
    path("details/<int:pk>/", details_ent, name="details"),
    path("delete/<int:pk>/", delete_ent, name="delete"),
    path("liste_class/", Entreprise_list.as_view(), name="liste_class"),
    path("details_class/<int:pk>/", Entreprise_detail.as_view(), name="details_class"),
    path("supprimer_class/<int:pk>/", Entreprise_delete.as_view(), name="supprimer_class"),
    path("create_class/", Entreprise_create.as_view(), name="create_class"),
    path("update_class/<int:pk>/", Entreprise_update.as_view(), name="update_class"),
]
