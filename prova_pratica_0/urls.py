from django.urls import path
from .views import somma,media,index3
app_name="prova_pratica_0"
urlpatterns=[
    path('somma',somma,name='somma'),
    path('media',media,name='media'),   
    path('',index3,name='index3'),
    
]