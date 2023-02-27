from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Articolo,Giornalista
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.core.serializers import serialize
import json

# Create your views here.

def home(request):
    articoli=Articolo.objects.all()
    giornalisti=Giornalista.objects.all()
    context={'articoli':articoli,'giornalisti':giornalisti}
    print(context)
    return render(request,"homepage2.html",context)

def articoloDetailView(request,pk):
    # articolo=Articolo.objects.get(pk=pk)
    articolo=get_object_or_404(Articolo,pk=pk)
    context={'articolo':articolo}
    return render(request,"articolo_detail.html",context)


class ArticoloDetailViewCB(DetailView):
    model=Articolo
    template_name="articolo_detail.html"

class ArticoloListView(ListView):
    model=Articolo
    template_name="lista_articoli.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['articoli']=Articolo.objects.all()
        return context

class GiornalistaDetailViewCB(DetailView):
    model=Giornalista
    template_name="giornalista_detail.html"

class GiornalistaListView(ListView):
    model=Giornalista
    template_name="lista_giornalisti.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['giornalisti']=Giornalista.objects.all()
        return context


def giornalisti_list_api(request):
    giornalisti=Giornalista.objects.all()
    data={'giornalisti':list(giornalisti.values("pk","nome","cognome"))}
    response=JsonResponse(data)
    return response

def giornalisti_api(request, pk):
    try:
        giornalista=giornalista.object.get(pk=pk)
        data={'giornalista':{
            "nome":giornalista.nome,
            "cognome":giornalista.cognome,
            }
        }
        response=JsonResponse(data)
    except Giornalista.DoesNotExist:
        response=JsonResponse({
            "error":{
                "code":404,
                "message":"Giornalista non trovato"
            }}
            ,status=404)
    return response