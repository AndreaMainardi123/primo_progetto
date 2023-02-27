from django.urls import path
from prova_pratica_1.views import view_a1, view_b1
app_name="prova_pratica_1"
urlpatterns=[
    path('auto', view_a1, name="auto"),
    path('noleggi', view_b1, name="noleggi"),
]