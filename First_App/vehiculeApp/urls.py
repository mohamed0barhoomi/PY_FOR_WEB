from django.urls import path
from .views import (
    home, list_veh, details_veh, delete_veh,
    Vehicule_list, Vehicule_detail, Vehicule_delete, Vehicule_create, Vehicule_update,
)

app_name = "vehicule"

urlpatterns = [
    path("", home, name="home"),
    path("list/", list_veh, name="list"),
    path("details/<int:pk>/", details_veh, name="details"),
    path("delete/<int:pk>/", delete_veh, name="delete"),
    path("liste_class/", Vehicule_list.as_view(), name="liste_class"),
    path("details_class/<int:pk>/", Vehicule_detail.as_view(), name="details_class"),
    path("supprimer_class/<int:pk>/", Vehicule_delete.as_view(), name="supprimer_class"),
    path("create_class/", Vehicule_create.as_view(), name="create_class"),
    path("update_class/<int:pk>/", Vehicule_update.as_view(), name="update_class"),
]
