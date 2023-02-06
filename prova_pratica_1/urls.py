from django.urls import path
from prova_pratica_2.views import view_a, view_b, view_c
app_name="prova_pratica_2"
urlpatterns=[
    path('auto', view_a, name="auto"),
    path('noleggi', view_b, name="noleggi"),
    path('totale', view_c, name="totale"),
]