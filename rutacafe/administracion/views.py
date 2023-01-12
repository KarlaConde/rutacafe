from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
import json

# Create your views here.

#programamos primero el acceso al framewokr a traves del restapi
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

#importamos los datos del archivo serializers
from .serializers import EmprendimientoSerializers, ClienteSerializers, EmprendedorSerializers,ServicioSerializers, ProductoSerializers,AdministradorSerializers,ReservaSerializers, CompraSerializers

#importar el modelo
from .models import Emprendimiento,Cliente,Emprendedor,Servicio,Producto,Administrador,Reserva,Compra,Categoria_Serv,Categoria_Emp
from django.views import View
#agregamos la importacion del formulario

from .forms import ReservaFormulario
#formas creando directamente encampsularlos
#1metodo
class Index(View):
    def get(self, request):
        categorias = Categoria_Emp.objects.all() # seria de agg categorias 
        print(categorias)
        return render(request, 'presentacion/index.html', {'categorias' : categorias})

# ================== clase para mostrar los emprendimientos de manera individual ¡¡¡¡
# listar emprendimientos
class ListarEmprendimientos(View):
    def get(self, request):
        emprendimientos = Emprendimiento.objects.all().order_by('categorias_emprendimiento')
        #emprendedores = Emprendedor.objects.all()
        #for emprendimiento in emprendimientos:
            #for emprededor in emprendedores:
                #if emprendimiento.id in emprededor.emprendimientos.iterator:
                    #salida = {
                        #'nombre_emprendedr': emprededor.nombres + ' ' + emprededor.apellidos
                    #}
                    #print(salida)
        return render(request, 'emprendimiento/lista_empren.html', {'emprendimientos': emprendimientos })
class ListarEmprendedores(View):
    def get(self, request):
       emprendedores = Emprendedor.objects.all().order_by('first_name')
        #emprendedores = Emprendedor.objects.all()
        #for emprendimiento in emprendimientos:
            #for emprededor in emprendedores:
                #if emprendimiento.id in emprededor.emprendimientos.iterator:
                    #salida = {
                        #'nombre_emprendedr': emprededor.nombres + ' ' + emprededor.apellidos
                    #}
                    #print(salida)
       return render(request, 'emprendedor/lista_empren.html', {'emprendedores': emprendedores })

# listar emprendimientos hoteleros
class ListarEmprendimientoshoteleria(View):
    def get(self, request, id_categoria):
        if not id_categoria:
            id_categoria=1
        empreder = Emprendimiento.objects.all().filter(categorias_emprendimiento=id_categoria)
        print(empreder)
        return render(request, 'hotelero/lista_empren.html', {'empreder': empreder})

# ver el emprendimiento
class VerEmprendimiento(View):
    def get(self, request, id_emprendimiento):
        emprendemiento = Emprendimiento.objects.all().filter(id=id_emprendimiento)
        form = ReservaFormulario()
        emprendemiento=emprendemiento
        print()
        return render(request, 'emprendimiento/emprendimiento.html', {
            'form': form,
            'emprendimiento': emprendemiento
        })

# ver el emprendedor
class VerEmprendedor(View):
    def get(self, request, id_emprendedor):
        emprendedores = Emprendedor.objects.all().filter(id=id_emprendedor)
        form = ReservaFormulario()
        emprendedores=emprendedores
        print(form)
        return render(request, 'emprendedor/emprendedor.html', {
            'form': form,
            'emprendedores': emprendedores
        })
#ver los productos 
class VerProducto(View):
    def get(self, request, id_producto):
        productos = Producto.objects.all().filter(id=id_producto)
        form = ReservaFormulario()
        productos=productos
        print()
        return render(request, 'emprendimiento/emprendedor.html', {
            'form': form,
            'producto': productos
        })

#----clase para llamar a las reservas de los emprendimientos------

class GenerarReserva(View):
   def get(self, request):
     return render(request, 'reservas/index.html', {})



class Emprendimiento_APIView(APIView):
    #metodo get para que puedan obtener la informacion
    def get(self, request, format=None, *args, **Kwargs):
        #realizar la consulta mediante el ORM de django para objeter todos los emprendimientos
        emprendimientos= Emprendimiento.objects.all()
        #utilizar la clase que habilital apra crear el ai y enviar los emprendimientos registrados
        serializer= EmprendimientoSerializers(emprendimientos, many=True)
        # responde la data de los emprendimientos
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer= EmprendimientoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
class Emprendimiento_APIView_Detalles(View):
    #vamos a obtener todos los objetos
    def get_objeto(self, emprendimiento_id):
        try:
            return Emprendimiento.objects.get(id=emprendimiento_id)
        except Emprendimiento.DoesNotExist:
            raise Http404
    
    def  get(self, request, id_emprendimiento, format=None):
        emprendimiento= self.get_objeto(id_emprendimiento)
        serializer= EmprendimientoSerializers(emprendimiento)
        return Response(serializer.data)
    
    #vamos a crear un metodo put
    
    def put(self, request, id_emprendimiento, format=None):
        emprendimiento= self.get_objeto(id_emprendimiento)
        serializer= EmprendimientoSerializers(emprendimiento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Emprendedor_APIView(APIView):
    #metodo get para que puedan obtener la informacion
    def get(self, request, format=None, *args, **Kwargs):
        #realizar la consulta mediante el ORM de django para objeter todos los emprendimientos
        emprendedores= Emprendimiento.objects.all()
        #utilizar la clase que habilital apra crear el ai y enviar los emprendimientos registrados
        serializer= EmprendedorSerializers(emprendedores, many=True)
        # responde la data de los emprendimientos
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer= EmprendedorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



class Emprendedor_APIView_Detalles(View):
    #vamos a obtener todos los objetos
    def get_objeto(self, emprendedor_id):
        try:
            return Emprendedor.objects.get(id=emprendedor_id)
        except Emprendedor.DoesNotExist:
            raise Http404
    
    def  get(self, request, emprendedor_id, format=None):
        emprendedores= self.get_objeto(emprendedor_id)
        serializer= EmprendedorSerializers(emprendedor_id)
        return Response(serializer.data)
    
    #vamos a crear un metodo put
    
    def put(self, request, emprendedor_id, format=None):
        emprendedores= self.get_objeto(emprendedor_id)
        serializer= EmprendedorSerializers(emprendedores, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Reserva_APIView(APIView):
    #metodo get para que puedan obtener la informacion
    def get(self, request, format=None, *args, **Kwargs):
        #realizar la consulta mediante el ORM de django para objeter todos los emprendimientos
        reservas= Reserva.objects.all()
        #utilizar la clase que habilital apra crear el ai y enviar los emprendimientos registrados
        serializer= ReservaSerializers(reservas, many=True)
        # responde la data de los emprendimientos
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer= ReservaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class Reserva_APIView_Detalles(View):
    #vamos a obtener todos los objetos
    def get_objeto(self, reserva_id):
        try:
            return Reserva.objects.get(id=reserva_id)
        except Reserva.DoesNotExist:
            raise Http404
    
    def  get(self, request, reserva_id, format=None):
        reservas= self.get_objeto(reserva_id)
        serializer= ReservaSerializers(reserva_id)
        return Response(serializer.data)
    
    #vamos a crear un metodo put
    
    def put(self, request, reserva_id, format=None):
        reservas= self.get_objeto(reserva_id)
        serializer= EmprendedorSerializers(reservas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservasGuardar(View):
    def get(self, request):
        
        form = ReservaFormulario()
        print(form)
        return render(request, 'reservas/index.html', {
                'form': form,     
            }
         )
    
    def post(self, request, *args, **kwargs):
        form = ReservaFormulario(request.POST or None, request.FILES or None)
        # Revisa si es valido:
        valor = kwargs
        print(request.POST)
        print(valor)
        if form.is_valid():
            # Procesa y asigna los datos con form.cleaned_data como se requiere
            fecha = form.cleaned_data['fecha']
            cedula = form.cleaned_data['cedula']
            nombres = form.cleaned_data ['nombres']
            telefono = form.cleaned_data ['telefono']
            tipo_emprendimiento = form.cleaned_data['tipo_emprendimiento']
            cantidad = form.cleaned_data['cantidad']
            tipo_producto = form.cleaned_data ['tipo_producto']
            reserva = Reserva(
                        fecha = fecha,
                        tipo_emprendimiento=tipo_emprendimiento,
                        cantidad=cantidad,
                        cedula = cedula,
                        nombres = nombres,
                        telefono = telefono,
                        )
            reserva.save()
            print(reserva.__dict__)
            reserva.tipo_producto.set(tipo_producto)
            
            form = ReservaFormulario()
            return HttpResponseRedirect("index")
        else:
            #De lo contrario lanzara el mismo formulario
            return render(request, 'emprendimiento/emprendimiento.html', {'form': form})
