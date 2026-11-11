from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import Vehicule
from .forms import VehiculeForm


# ---------- vues fonctions ----------

def home(request):
    return render(request, "vehicule/home.html")


def list_veh(request):
    list = Vehicule.objects.select_related("entrprise")
    return render(request, "vehicule/list.html", {"list": list})


def details_veh(request, pk):
    veh = get_object_or_404(Vehicule, pk=pk)
    return render(request, "vehicule/details.html", {"veh": veh})


def delete_veh(request, pk):
    veh = get_object_or_404(Vehicule, pk=pk)
    veh.delete()
    return redirect("vehicule:list")


# ---------- vues classes ----------

class Vehicule_list(ListView):
    model = Vehicule
    template_name = "vehicule/list.html"
    context_object_name = "list"


class Vehicule_detail(DetailView):
    model = Vehicule
    template_name = "vehicule/details.html"
    context_object_name = "veh"


class Vehicule_delete(DeleteView):
    model = Vehicule
    template_name = "vehicule/confirm_delete.html"
    context_object_name = "veh"
    success_url = reverse_lazy("vehicule:liste_class")


class Vehicule_create(CreateView):
    model = Vehicule
    form_class = VehiculeForm
    template_name = "vehicule/form.html"
    success_url = reverse_lazy("vehicule:liste_class")


class Vehicule_update(UpdateView):
    model = Vehicule
    form_class = VehiculeForm
    template_name = "vehicule/form.html"
    success_url = reverse_lazy("vehicule:liste_class")
