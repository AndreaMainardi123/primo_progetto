from django.urls import path
from .views import home, ArticoloDetailViewCB,ArticoloListView,GiornalistaDetailViewCB,GiornalistaListView,giornalisti_list_api,giornalisti_api

app_name="news"

urlpatterns = [
    path('', home, name="homeview"),
    path('articoli/<int:pk>',ArticoloDetailViewCB.as_view(),name="articolo_detail"),
    path('lista_articoli/',ArticoloListView.as_view(),name="lista_articoli"),
    path('giornalisti/<int:pk>',GiornalistaDetailViewCB.as_view(),name="giornalista_detail"),
    path('lista_giornalisti/',GiornalistaListView.as_view(),name="lista_giornalisti"),
    path('lista_giornalisti_api/',giornalisti_list_api,name="giornalisti_list_api"),
    path('giornalisti_api/<int:pk>',giornalisti_api,name="giornalisti_api"),
    ]