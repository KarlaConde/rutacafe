from django import forms
from .models import Producto,Emprendimiento,Reserva
from django.shortcuts import render
from django.forms import ModelForm

# creating a form

class ReservaForm(forms.Form):
    class Meta:
        model=Reserva
        fields='__all__'

class ReservaFormulario(forms.ModelForm):
    
    def presentarEmpre(self):
        pass
    
    def __init__(self, *args, **kwargs):
        super(ReservaFormulario,self).__init__(*args, **kwargs)
        print('este es el kw', self)
        self.fields['tipo_producto'].queryset = Producto.objects.all()
        
        
    class Meta:
        model = Reserva
        fields = [
            'fecha',
            'cedula',
            'nombres',
            'telefono',
            'cantidad',
            'tipo_emprendimiento',
            'tipo_producto',
            
            
            ]
        labels = {
        'fecha':'Fecha de Reserva',
        'cedula' : 'Cedula',
        'nombre' : 'Nombre Cliente',
        'telefono' : 'Celular',
        'cantidad': 'Numero de productos',
        'tipo_emprendimiento':'Negocio',
        
        
        
        
        }
        widgets = {
            'fecha': forms.DateInput(format=('%d-%m-%Y'), attrs={ 'type':'date' }),
            #'tipo_producto':forms.MultipleChoiceField(choices=[(item.pk, item) for item in Producto.objects.all()], to_field_name="Productos"),
            #'tipo_producto': forms.MultipleChoiceField(queryset=Producto.objects.all(), empty_label="Productos",to_field_name="Productos"),
        }
    tipo_producto = forms.ModelMultipleChoiceField(queryset=Producto.objects.all(), widget=forms.CheckboxSelectMultiple)
    

