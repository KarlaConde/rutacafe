from django.contrib import admin

# Register your models here.
from.models import Emprendimiento, Emprendedor, Cliente, Administrador,Producto, Reserva, Servicio,Categoria_Emp, Categoria_Serv


admin.site.register(Emprendedor)
admin.site.register(Emprendimiento)
admin.site.register(Cliente)
admin.site.register(Administrador)
admin.site.register(Producto)
admin.site.register(Reserva)
admin.site.register(Servicio)
admin.site.register(Categoria_Emp)
admin.site.register(Categoria_Serv)
