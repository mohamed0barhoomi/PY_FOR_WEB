from django.urls import path
from .views import list_off,details_off,delete_off,home

app_name = "offre"

urlpatterns =[
    path("/",home,name="home"),
    path("/list_off",list_off,name="list_off"),
    path("/details_off/<int:pk>",details_off,name="details_off"),
    path("delete/<int:pk>",delete_off,name="delete")
]
