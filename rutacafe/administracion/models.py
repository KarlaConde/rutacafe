from distutils.command.upload import upload
from pyexpat import model
from random import choices
from secrets import choice
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

# Create your models here.
class Categoria_Emp(models.Model):
    
    categoria_emprendimiento=models.CharField(verbose_name="Categoria",max_length=150)
    descripcion=models.TextField()
    foto = models.ImageField(upload_to="fotos_categorías/", verbose_name="Foto categoria", null = True, blank=True)

    
    class meta:
        verbose_name= "Categoria"
        verbose_name_plural="Categorias"
        
    def __str__(self) -> str:
        return self.categoria_emprendimiento
    
class Emprendimiento(models.Model):
   
    #de muchos a muchos
    categorias_emprendimiento= models.ForeignKey(Categoria_Emp,on_delete=models.CASCADE, verbose_name='Categoria', null=True, blank=True)
    nombre_emprendimiento=models.CharField(verbose_name="Emprendimiento",max_length=150)
    direccion=models.CharField(verbose_name="direccion",max_length=150)
    celular=models.CharField(verbose_name="Celular",max_length=13)
    tel_fijo=models.CharField(verbose_name="Telf.Fijo",max_length=13)
    descripcion=models.TextField()
    hora_apertura=models.DateTimeField()
    hora_cierre=models.DateTimeField()
    altitud=models.CharField(verbose_name="altitud",max_length=20)
    latitud=models.CharField(verbose_name="latitud",max_length=20)
    fotoemp=models.ImageField(upload_to="fotos_emprendimiento/",verbose_name="Subir una foto", null=True,blank=True)
    video=models.URLField(verbose_name="Video Promocional", null=True,blank=True)
    face = models.URLField(verbose_name = "Facebook", null=True, blank= True)
    instagram = models.URLField(verbose_name = "Instagram", null=True, blank= True)
    titter = models.URLField(verbose_name = "Twitter", null=True, blank= True)
    slug = models.SlugField(max_length=100, unique=True)

    class meta:
        verbose_name= "Emprendimiento"
        verbose_name_plural="Emprendimientos"
        
    def __str__(self) -> str:
        return self.nombre_emprendimiento
    
    def slug(self):
        return slugify(self.nombre_emprendimiento)
    
class Persona(AbstractUser):
    TIPO_DOCUMENTO_CH=[
        ('cedula','Cedula'),
        ('pasaporte','Pasaporte')
    ]
    username=models.CharField(max_length=100, unique=True)
    email= models.EmailField(max_length=150, unique=True,blank=True,null=True,verbose_name="Correo")
    tipo_documento= models.CharField(verbose_name="Tipo de documento",max_length=20, choices=TIPO_DOCUMENTO_CH)
    cedula= models.CharField(verbose_name="Cedula",max_length=13,blank=True,null=True)
    first_name= models.CharField(verbose_name="Nombres",max_length=100,blank=True,null=True)
    last_name= models.CharField(verbose_name="Apellidos",max_length=100,blank=True,null=True)
    celular=models.CharField(verbose_name="N.Celular",max_length=13,blank=True,null=True)
    direccion=models.CharField(verbose_name="Direccion",max_length=20,blank=True,null=True)
    fecha_nacimiento=models.DateField(verbose_name="Fecha_nacimiento",blank=True,null=True)
    foto=models.ImageField(upload_to="Fotos_usuarios/",verbose_name="Subir una foto", null=True,blank=True)
    
    
    class meta:
        verbose_name= "Persona"
        verbose_name_plural="Personas"
    #metodo para presentar el objeto creado
    def __str__(self):
        return self.cedula+self.last_name+self.first_name
    
class Cliente(Persona):
    pais_origen=models.CharField(verbose_name="País de Origen",max_length=13)
    class meta:
        verbose_name= "Cliente"
        verbose_name_plural="Clientes"
    def __str__(self):
            return self.cedula+self.nombres+self.apellidos+self.pais_origen
      
class Administrador(Persona):
    fecha_inicio=models.DateTimeField()
    fecha_actualizacion=models.DateTimeField()
    estado=models.BooleanField()
    class meta:
        verbose_name= "Administrador"
        verbose_name_plural="Administradores"
    def __str__(self):
            return self.cedula+self.nombres+self.apellidos
class Emprendedor(Persona):
    #de muchos a muchos
    emprendimientos= models.ManyToManyField(Emprendimiento, blank=True)
    class meta:
        verbose_name= "Emprendedor"
        verbose_name_plural="Emprendedores"
    def __str__(self):
            return self.cedula
class Producto(models.Model):
    tipo_emprendimiento= models.ForeignKey(Emprendimiento, on_delete=models.PROTECT, verbose_name='Emprendimiento_tipo',null=True,blank=True)
    nombre_prod=models.CharField(verbose_name="Nombre producto",max_length=150)
    descripcion=models.TextField()
    Precio=models.FloatField(verbose_name="Precio")
    fecha_elaboracion=models.DateField(null=True, blank=True)
    fecha_caducidad=models.DateField(null=True)
    cantidad=models.IntegerField(verbose_name="Cantidad")
    foto_prod=models.ImageField(upload_to="Fotos_producto/",verbose_name="Subir una foto",blank=True)
    class meta:
        verbose_name= "Producto"
        verbose_name_plural="Productos"
    def __str__(self):
            return self.nombre_prod +" "+ str(self.cantidad)
        
class Reserva(models.Model):
    cedula=models.CharField(verbose_name="Cedula", max_length=10, null=True, blank=True)
    nombres=models.CharField(verbose_name="Nombre", max_length=100, null=True, blank=True)
    telefono=models.CharField(verbose_name="Telefono", max_length=10, null=True, blank=True)
    #Agregar Detalles producto
    cantidad=models.IntegerField(verbose_name="Cantidad", null=True, blank=True)
    fecha= models.DateTimeField(null=True, blank=True)
    #Precior=models.FloatField(verbose_name="Precio" ,null=True, blank=True)
    #tipo_producto= models.ForeignKey(Producto, on_delete=models.PROTECT, verbose_name='Producto_tipo') #,null=True,blank=True
    tipo_producto= models.ManyToManyField(Producto, blank=True, related_name='producto')
    tipo_emprendimiento= models.ForeignKey(Emprendimiento, on_delete=models.PROTECT, verbose_name='Emprendimiento_tipo', null=True,blank=True)
    
    
    class Meta: 
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        
    def __str__(self):
        return self.cedula
    
class Categoria_Serv(models.Model):
    
    tipo_servicio=models.CharField(verbose_name="Tipo de Servicio",max_length=150)
    descripcion=models.TextField()
    
    class meta:
        verbose_name= "Categoria"
        verbose_name_plural="Categorias"
        
    def __str__(self) -> str:
        return self.tipo_servicio
    

class Servicio(models.Model):
    #de muchos a muchos
    categoriaserv= models.ManyToManyField(Categoria_Serv, blank=True)
    calificacion=models.IntegerField(verbose_name="Calificación")
    comerntario_sugerencia=models.TextField(verbose_name="Comentarios y Sugerencias")
    class meta:
        verbose_name= "Servicio"
        verbose_name_plural="Servicios"
    def __str__(self):
            return self.comerntario_sugerencia
class Compra(models.Model):
    #de muchos a muchos
    productos= models.ManyToManyField(Producto, blank=True)
    cantidad=models.IntegerField(verbose_name="Cantidad")
    subtotal=models.IntegerField(verbose_name="Subtotal")
    total=models.IntegerField(verbose_name="Total")
    class meta:
        verbose_name= "Compra"
        verbose_name_plural="Compras"
    def __str__(self):
            return self.tipo_ser
class Galeria(models.Model):
    #de muchos a muchos
    galerias= models.ManyToManyField(Producto, blank=True)
    foto=models.ImageField(upload_to="Fotos_usuarios/",verbose_name="Subir una foto", null=True,blank=True)
    videog=models.URLField(verbose_name="Video Promocional", null=True,blank=True)
    class meta:
        verbose_name= "Galeria"
        verbose_name_plural="Galerias"
    