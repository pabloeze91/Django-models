from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def hola_mundo(request):    
    datos =  {"mensaje": "hola_mundo", "curso": "python-django"}
    return JsonResponse(datos)

def get_comic_api_view(request):
    print("Endpoint get_comic_api_view")
    # Alumno, aquí deberá completar el endpoint
