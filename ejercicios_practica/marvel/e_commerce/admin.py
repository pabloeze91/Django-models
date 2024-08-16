from django.contrib import admin

from e_commerce.models import Comic #OJO!! importamos desde el directorio manage.py

# NOTE: Tenemos que importar los modelos con los que vamos a trabajar:
from e_commerce.models import *

# Register your models here.

@admin.register(Comic)
#clase que me permite registrar ese modelo en el administrador django
class ComicsAdmin(admin.ModelAdmin):
    # NOTE: Para seleccionar los campos en la tabla de registros
    list_display = ('id','marvel_id', 'title', 'stock_qty', 'price')

    # NOTE: Filtro lateral de elementos:
    list_filter= ('marvel_id','title')
    
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['title', 'description']

    # NOTE: Para seleccionar los campos en el registro.
    # cuando agregue un comic, solo voy a completar esos campos 
    #fields = ('marvel_id', 'title', 'stock_qty')

#Otra opción (no pueden estar descomentadas ambas) que me permite colapsar los demás campos
#es una tupla de tuplas
    # NOTE: Genera un campo desplegable con los registros seleccionados.
    fieldsets = (
        (None, {
            'fields': ('marvel_id', 'title', 'stock_qty')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('description','price', 'picture'),
        }),
    )
    pass
@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    pass
