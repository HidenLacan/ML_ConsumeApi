from django.shortcuts import render
from django.views import View
import requests


# Create your views here.


class Agucate_prediccion(View):
    
    def post(self,request):
        
        # recuperar datos del formulario
        color = request.POST.get('color')
        tamano = request.POST.get('tamano')
        firmeza = request.POST.get('firmeza')
        
        #construir la solicitud para la API
        datos_api = {
            'color':color,
            'tamano':tamano,
            'firmeza':firmeza
        }
        
        # Hacer la solicitud a la API
        
        respuesta = requests.post('https://avocadoprediction.onrender.com/api/prediccion/',json=datos_api)
        
        ## Logica de la respuesta
        if respuesta.status_code == 200:
            resultado = respuesta.json()
            return render(request,'resultado.html',{"resultado":resultado})
        else:
            return render(request,'error.html',{'error':respuesta.status_code})
    
        
    
    def get(self,request):
        return render(request,'test.html')