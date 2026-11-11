from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import Entreprise
from .forms import EntrepriseForm


def home(request):
    return render(request, "entreprise/home.html")


def list_ent(request):
    list = Entreprise.objects.select_related("gerant")
    return render(request, "entreprise/list.html", {"list": list})


def details_ent(request, pk):
    ent = get_object_or_404(Entreprise, pk=pk)
    return render(request, "entreprise/details.html", {"ent": ent})


def delete_ent(request, pk):
    ent = get_object_or_404(Entreprise, pk=pk)
    ent.delete()
    return redirect("entreprise:list")



class Entreprise_list(ListView):
    model = Entreprise
    template_name = "entreprise/list.html"
    context_object_name = "list"


class Entreprise_detail(DetailView):
    model = Entreprise
    template_name = "entreprise/details.html"
    context_object_name = "ent"


class Entreprise_delete(DeleteView):
    model = Entreprise
    template_name = "entreprise/confirm_delete.html"
    context_object_name = "ent"
    success_url = reverse_lazy("entreprise:liste_class")


class Entreprise_create(CreateView):
    model = Entreprise
    form_class = EntrepriseForm
    template_name = "entreprise/form.html"
    success_url = reverse_lazy("entreprise:liste_class")


class Entreprise_update(UpdateView):
    model = Entreprise
    form_class = EntrepriseForm
    template_name = "entreprise/form.html"
    success_url = reverse_lazy("entreprise:liste_class")
