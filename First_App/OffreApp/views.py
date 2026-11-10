from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Offre
# Create your views here.

def home(request):
    return render(request,"Offre/home.html")
def list_off(request):
    list=Offre.objects.all()
    return render(request,'offre/list.html',{"list":list})
def details_off(request,pk):
    off=Offre.objects.get(pk=pk)
    return render(request,"offre/details.html",{"off":off})
def delete_off(request,pk):
    off=Offre.objects.get(pk=pk)
    off.delete()
    return redirect("offre/list.html")



