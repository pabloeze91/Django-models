from django.db import models

# NOTE: Para poder utilizar el modelo "user" que viene por defecto en Django,
# Debemos importarlo previamente:
from django.contrib.auth.models import User

# Create your models here.
#No es una clase común y corriente sino que representa un modelo
class Comic(models.Model):
    '''
    Esta clase hereda de Django models.Model y crea una tabla llamada
    e_commerce_comic. Las columnas toman el nombre especificado de cada objeto.
    '''
    #atributos (columnas) son los mismos que hay en Adminer en e_commerce_comics
    id = models.BigAutoField(db_column='ID', primary_key=True) #todo es una instancia de la clase BigAutoField, donde a esa instancia le pasamos parámetros
    marvel_id = models.PositiveIntegerField(
        verbose_name='marvel id', null=False, blank=False, unique=True
        #el verbose_name es como lo va a visualizar el usuario
    )
    title = models.CharField(
        verbose_name='title', max_length=120, default=''
    )
    description = models.TextField(verbose_name='description', default='')
    price = models.FloatField(
        verbose_name='price', max_length=5, default=0.00
    )
    stock_qty = models.PositiveIntegerField(
        verbose_name='stock qty', default=0
    )
    picture = models.URLField(verbose_name='picture', default='') #con URLField el string va a tener ciertas validaciones

    #método str: cuando hago un print de una instancia de mi modelo Comic (comic = Comic.objects.create(title='Spiderman', description='',...)), es decir, print(comic), lo que voy a ver es lo que devuelve mi método str, que en este caso es el id
    def __str__(self):
        '''
        El método __str__ cumple una función parecida a __repr__ en SQL Alchemy, 
        es lo que retorna cuando llamamos al objeto.
        '''
        return f'{self.id} - {self.title}'

    #Defino una clase dentro de otra clase, en Python lo puedo hacer
    class Meta:
        '''
        Con "class Meta" podemos definir atributos de nuestras entidades como el nombre de la tabla.
        '''
        db_table = 'e_commerce_comics' #nombre de la tabla
        verbose_name = 'comic' #child
        verbose_name_plural = 'comics' #children

class WishList(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    user = models.ForeignKey(
        User,
        verbose_name = 'user',
        blank=True,
        on_delete=models.CASCADE
    )
    comic = models.ForeignKey(
        Comic,
        verbose_name='comic',
        on_delete=models.CASCADE,
        default=1,
        blank=True
    )
    favorite = models.BooleanField(default=False, verbose_name='favorite')
    cart = models.BooleanField(default=False, verbose_name='cart')
    wished_qty = models.PositiveIntegerField(default=0, verbose_name='wished qty')
    bought_qty = models.PositiveIntegerField(default=0, verbose_name='bought qty')
    class Meta:
        db_table = 'e_commerce_wish_list'
        verbose_name = 'wish list'
        verbose_name_plural = 'wish lists'
    favorite = models.BooleanField(verbose_name='favorite')
    cart = models.BooleanField(verbose_name='cart')
    wished_qty = models.PositiveBigIntegerField(verbose_name='wished qty', default=0)
    bought_qty = models.PositiveIntegerField(verbose_name='bought qty', default = 0)
