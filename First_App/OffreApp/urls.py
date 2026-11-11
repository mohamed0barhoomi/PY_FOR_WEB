from django.urls import path
from .views import (
    home, list_off, details_off, delete_off,
    Offre_list, Offre_detail, Offre_delete, Offre_create, Offre_update,
)

app_name = "offre"

urlpatterns = [
    path("", home, name="home"),
    path("list_off/", list_off, name="list_off"),
    path("details_off/<int:pk>/", details_off, name="details_off"),
    path("delete/<int:pk>/", delete_off, name="delete"),
    path("liste_class/", Offre_list.as_view(), name="liste_class"),
    path("details_class/<int:pk>/", Offre_detail.as_view(), name="details_class"),
    path("supprimer_class/<int:pk>/", Offre_delete.as_view(), name="supprimer_class"),
    path("create_class/", Offre_create.as_view(), name="create_class"),
    path("update_class/<int:pk>/", Offre_update.as_view(), name="update_class"),
]
