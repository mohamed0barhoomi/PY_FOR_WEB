from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Expedition
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
from .froms import Expeditionsform

def home(request):
    return render(request,"Expedition/home.html")
def welcome(request,name):
    return HttpResponse(f'hello {name}')
def list_exp(request):
    list=Expedition.objects.all()
    return render(request,'Expedition/list.html',{"list":list})
def details_exp(request,pk):
    exp=get_object_or_404(Expedition,pk=pk)
    return render(request,'Expedition/details.html',{"exp":exp})
def delete_exp(request,pk):
    exp=get_object_or_404(Expedition,pk=pk)
    exp.delete()
    return redirect("expedition:list")



class Expedition_list(ListView):
    model = Expedition
    template_name = 'Expedition/list.html'
    context_object_name = 'list'

class Expedition_detail(DetailView):
    model = Expedition
    template_name = 'Expedition/details.html'
    context_object_name = 'exp'

class Expedition_delete(DeleteView):
    model = Expedition
    template_name = 'Expedition/confirm_delete.html'
    context_object_name = 'exp'
    success_url = reverse_lazy('expedition:liste_class')  # Redirige vers la liste après la suppression

class expedition_create(CreateView):
    model=Expedition
    form_class = Expeditionsform
    template_name='Expedition/form.html'
    success_url=reverse_lazy('expedition:liste_class')

class expedition_update(UpdateView):
    model= Expedition
    form_class= Expeditionsform
    template_name='Expedition/form.html'
    success_url=reverse_lazy('expedition:liste_class')




# Create your views here.
