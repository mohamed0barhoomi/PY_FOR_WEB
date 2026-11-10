from django.urls import path, include
from .models import Expedition
from .views import welcome,home,list_exp,details_exp,delete_exp,Expedition_list,Expedition_detail,Expedition_delete,expedition_create,expedition_update
app_name = "expedition"
urlpatterns = [
    path('list/',list_exp,name="list"),
    path("home/",home,name="home"),
    path("welcome/<str:name>/",welcome,name="welcome"),
    path("details/<int:pk>/",details_exp,name="details"),
    path("delete/<int:pk>/",delete_exp,name="delete"),
    path("liste_class/", Expedition_list.as_view(), name="liste_class"),
    path("details_class/<int:pk>/", Expedition_detail.as_view(), name="details_class"),
    path("supprimer_class/<int:pk>/", Expedition_delete.as_view(), name="supprimer_class"),
    path("create_class/", expedition_create.as_view(), name="create_class"),
    path("update_class/<int:pk>/", expedition_update.as_view(), name="update_class"),
]