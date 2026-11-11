from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import Offre
from .forms import OffreForm



def home(request):
    return render(request, "offre/home.html")


def list_off(request):
    list = Offre.objects.select_related("entreprise", "expedition", "vehicule")
    return render(request, "offre/list.html", {"list": list})


def details_off(request, pk):
    off = get_object_or_404(Offre, pk=pk)
    return render(request, "offre/details.html", {"off": off})


def delete_off(request, pk):
    off = get_object_or_404(Offre, pk=pk)
    off.delete()
    return redirect("offre:list_off")




class Offre_list(ListView):
    model = Offre
    template_name = "offre/list.html"
    context_object_name = "list"


class Offre_detail(DetailView):
    model = Offre
    template_name = "offre/details.html"
    context_object_name = "off"


class Offre_delete(DeleteView):
    model = Offre
    template_name = "offre/confirm_delete.html"
    context_object_name = "off"
    success_url = reverse_lazy("offre:liste_class")


class Offre_create(CreateView):
    model = Offre
    form_class = OffreForm
    template_name = "offre/form.html"
    success_url = reverse_lazy("offre:liste_class")


class Offre_update(UpdateView):
    model = Offre
    form_class = OffreForm
    template_name = "offre/form.html"
    success_url = reverse_lazy("offre:liste_class")
