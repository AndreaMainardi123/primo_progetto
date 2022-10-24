from django.shortcuts import render
import random

'''def es_if(request):
    context= {
        'var1' : 200,
        'var2' : 200,
        'var3' : 300
    }
    return render(request, "es_if.html",context)'''
def somma(request):
    context={
        'x':random.randint(1, 10),
        'y':random.randint(1, 10)
    }
    return render(request,"somma.html")

def media(request):
    return render(request,"media.html")

def index3(request):
    return render(request,"index3.html")