from django.shortcuts import render

def view_a(request):
    context={
       
        'var1':'Matematica',
        'var2':'Italiano',
        'var3':'Inglese',
        'var4':'Storia',
        'var5':'Geografia',
    }
    return render(request, "view_a.html",context)

def view_b(request):
    context={
       'students': {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
                    'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
                    'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    }
    
 #   return view_b('view_b.html',
 #   {'data': sorted(view_b.items())})

def view_c(request):
  #  dati=students["Nicola Spina"]
   # print(dati)
    #media=0

    #for dato in dati:
     #   media+=dato[1]
    #media=media/len(dati)
    #print("Media="+str(media))
    return render(request,"view_c.html")