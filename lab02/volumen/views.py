from django.shortcuts import render
import math
# Create your views here.
def index(request):
    context = {
        'titulo' : "Calculo del Volumen de un Cilindro",
    } 
    return render(request, 'volumen/datos.html', context) 
def enviar(request):
    if request.method == 'POST':
        diametro=request.POST['diametro']
        altura=request.POST['altura']
        radio=float(diametro)/2
        area_base=math.pi*pow(radio, 2)
        respuesta=area_base*float(altura)
        
    context = {
        'titulo' : 'Respuesta del Volumen de un cilindro',
        'diametro' : request.POST['diametro'],
        'altura' : request.POST['altura'],
        'respuesta' : respuesta,
    }
    return render(request, 'volumen/resultvolumen.html', context)

