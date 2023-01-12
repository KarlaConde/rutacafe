from django.urls import path
from .import  views
from .views import*

app_name= 'administracion'


urlpatterns = [
    path('index', Index.as_view(), name="index"),
    # grupo de paths para los emprendimientos
    path('emprendimientos/listado',ListarEmprendimientos.as_view(),name='listado_emprendimientos' ),
    path('emprendedores/listado',ListarEmprendedores.as_view(),name='listado_emprendimientos' ),
    path('reserva',ReservasGuardar.as_view(),name='reserva'),
    path('emprendimientos/listado/<int:id_categoria>',ListarEmprendimientoshoteleria.as_view(),name='listado' ),
    path('emprendedores/emprendedor/<int:id_emprendedor>',VerEmprendedor.as_view(),name='ver_emprendedor' ),
    path('emprendimientos/emprendimiento/<int:id_emprendimiento>',VerEmprendimiento.as_view(),name='ver_emprendimiento' ),
    path("api/emprendimientos", Emprendimiento_APIView.as_view(),name='lista_emprendimientos'),
    path("api/emprendimientos/<int:id_emprendimiento>", Emprendimiento_APIView_Detalles.as_view(),name='detalle_emprendimiento'),
    path("api/emprendedores", Emprendedor_APIView.as_view(),name='lista_emprendedoress'),
    path("api/emprendedores/<int:id_emprendedor>", Emprendedor_APIView_Detalles.as_view(),name='detalle_emprendimiento'),
   
]
