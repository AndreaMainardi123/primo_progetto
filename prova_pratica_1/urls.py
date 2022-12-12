from django.urls import path
from .views import view_a,view_b,view_c
app_name="prova_pratica_1"
urlpatterns=[
    path('view_a',view_a,name='view_a'),
    path('view_b',view_b,name='view_b'),
    path('view_c',view_c,name='view_c'),
   # path('lista',lista,name='lista'),
   # path('chi_siamo',chi_siamo,name='chi_siamo'),
   # path('variabili',variabili,name='variabili'),
   # path('',index,name='index'),
    
]