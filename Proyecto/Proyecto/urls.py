from django.contrib import admin
from django.urls import path, include
from BaseDeDatos import views as bd_views
from django.conf import settings
from core import views as core_views
from django.conf.urls.static import static
from BaseDeDatos.views import ListclienteListView,ListclientePDF,ListOrdenListView,ListordenPDF


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',core_views.index,name='home'),
    path('contact/',core_views.contacto, name='contact'),
    path('portfolio/',core_views.portafolio),

    #Paths del Loguin
    path ('ingreso/',core_views.ingreso_registro),
    path('accounts/',include('django.contrib.auth.urls')),
    path ('salir/',core_views.cerrar_sesion,name="cerrar_sesion"),
    
    #CRUD CLIENTE
    path('clientes/',bd_views.GestionarCliente),
    path('RegistrarCliente/',bd_views.RegistrarCliente),
    path('eliminarcli/<id_cli>',bd_views.Eliminarcli),
    path('editarCli/<id_cli>',bd_views.editarcli),
    path('editarCliente/',bd_views.edicionClie),
    
    #CRUD PEDIDO
    path('pedidos/',bd_views.GestionarPedido),
    path('RegistrarPedido/',bd_views.RegistrarPedido),
    path('eliminarped/<cod_ped>',bd_views.ELiminarped),
    path('editarped/<cod_ped>',bd_views.editarped),
    path('editarPedido/<cod_ped>',bd_views.edicionPedi),
    
    #CRUD ORDEN
    path('ordenes/',bd_views.ListarOrden),
    path('RegistrarOrden/',bd_views.RegistrarOrden),
    path('eliminarord/<cod_ord>',bd_views.EliminarOrd),
    path('editarord/<cod_ord>',bd_views.editarorden),
    path('editarOrden/<cod_ord>',bd_views.edicionOrden),
    
    
    #CRUD MAQUINA
    path('maquinas/',bd_views.GestionarMaquina),
    path('RegistrarMaqui/',bd_views.RegistrarMaqui),
    path('eliminarmaq/<cod_maquina>',bd_views.Eliminarmaqui),
    path('editarmaq/<cod_maquina>',bd_views.editarmaqui),
    path('editarMaquina/<cod_maquina>',bd_views.edicionMaqui),
    
    #CRUD AREA
    path('areas/',bd_views.GestionaARea),
    path('RegistrarArea/',bd_views.RegistrarArea),
    path('eliminararea/<cod_area>',bd_views.Eliminararea),
    path('editarare/<cod_area>',bd_views.editarare),
    path('editarArea/',bd_views.edicionArea),
    
    #CRUD PIEZA
    path('piezas/',bd_views.GestionPieza),
    path('RegistrarPieza/',bd_views.RegistrarPieza),
    path('eliminarpieza/<cod_pieza>',bd_views.EliminarPieza),
    path('editarpie/<cod_pieza>',bd_views.editarpie),
    path('editarPieza/',bd_views.edicionPieza),
    
    #CONSULTAS Cliente-Pedido
    path('listarcli/',bd_views.ListaClientes_pedidos),
    path('pdf/',ListclienteListView.as_view(),name='pdf'),
    path('listarClientes/',ListclientePDF.as_view(),name=''),
    
    #CONSULTA Orden de produccion
    path('ordenPro/<cod_ord>',bd_views.ordenProduccion),
    path('ord/',ListOrdenListView.as_view(),name='ord'),
    path('mostrarOrden/',ListordenPDF.as_view(),name=''),

    
    
    
    
]

# codigo para verificar las imagenes cargadas
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)