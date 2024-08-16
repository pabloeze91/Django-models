from django.http import JsonResponse

# Create your views here.
def hola_mundo_api_view(request):    
    datos =  {"mensaje": "hola_mundo", "curso": "python-django"}
    return JsonResponse(datos)

def get_comic_api_view(request):
    datos = {
        "id": 1, 
        "marvel_comic": "1010", 
        "title": "Inove",
        "stock_qty": 6,
        "description": "Mi primer JSON en Django",
        "price": 10.0,
        "picture": "https://www.django-rest-framework.org/img/logo.png"        
    }
    return JsonResponse(datos)
