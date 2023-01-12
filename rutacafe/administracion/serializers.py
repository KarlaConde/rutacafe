from rest_framework import serializers
from.models import Emprendimiento,Emprendedor,Servicio,Cliente,Producto,Administrador, Reserva, Compra

#Completar los demas servicios

class EmprendimientoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Emprendimiento
        fields= '__all__'
       # exclude = ['created']
class EmprendedorSerializers(serializers.ModelSerializer):
    class Meta:
        model= Emprendedor
        fields= '__all__'
       # exclude = ['created']
class ServicioSerializers(serializers.ModelSerializer):
    class Meta:
        model= Servicio
        fields= '__all__'
       # exclude = ['created']
class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields= '__all__'
       # exclude = ['created']
class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields= '__all__'
       # exclude = ['created']
class AdministradorSerializers(serializers.ModelSerializer):
    class Meta:
        model= Administrador
        fields= '__all__'
       # exclude = ['created']
class ReservaSerializers(serializers.ModelSerializer):
    class Meta:
        model= Reserva
        fields= '__all__'
       # exclude = ['created']
class CompraSerializers(serializers.ModelSerializer):
    class Meta:
        model= Compra
        fields= '__all__'
       # exclude = ['created']
