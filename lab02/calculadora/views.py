from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def formulario(request):
    return render(request, 'calculadora/formulario.html')

def calcular(request):
    if request.method == 'POST':
        numero1 = float(request.POST['numero1'])
        numero2 = float(request.POST['numero2'])
        operacion = request.POST['operacion']
        
        if operacion == 'suma':
            resultado = numero1 + numero2
        elif operacion == 'resta':
            resultado = numero1 - numero2
        elif operacion == 'multiplicacion':
            resultado = numero1 * numero2
        elif operacion == 'divicion':
            resultado = numero1 / numero2
        
        return render(request, 'calculadora/resultado.html', {'resultado': resultado})
    else:
        return HttpResponseRedirect(reverse('formulario'))