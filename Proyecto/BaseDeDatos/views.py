from django.shortcuts import render,redirect
from .models import Cliente,Contacto,Maquina,Orden,Pedido,Pieza,Area
from django.contrib import messages
from django.views.generic import ListView,View
from django.http import HttpResponse
from BaseDeDatos.utils import render_to_pdf



# CRUD CLIENTES
def GestionarCliente(request):
    ListaClien=Cliente.objects.all()
    return render(request,'BaseDeDatos/GestionCliente.html',{'clientes':ListaClien})

def RegistrarCliente(request):
    id_cli=request.POST['cod']
    nom_cli=request.POST['txtnom']
    apell_cli=request.POST['txtape']
    tel_cli=request.POST['telefo']
    dir_cli=request.POST['dir']
    email_cli=request.POST['email']
    
    cliente=Cliente.objects.create(id_cli=id_cli,nom_cli=nom_cli,apell_cli=apell_cli,tel_cli=tel_cli,dir_cli=dir_cli,email_cli=email_cli)
    messages.success(request, '¡Cliente Creado Exitosamente!')   
    return redirect('/clientes/') 

def Eliminarcli(request,id_cli):
    cli=Cliente.objects.get(id_cli=id_cli)
    cli.delete()
    messages.success(request, '¡Cliente Eliminado!')
    return redirect('/clientes/')

def editarcli(request,id_cli):
    cli=Cliente.objects.get(id_cli=id_cli)
    return render(request,'BaseDeDatos/edicionCli.html',{'clientes':cli})

def edicionClie(request):
    id_cli=request.POST['cod']
    nom_cli=request.POST['txtnom']
    apell_cli=request.POST['txtape']
    tel_cli=request.POST['telefo']
    dir_cli=request.POST['dir']
    email_cli=request.POST['email']
    
    cli=Cliente.objects.get(id_cli=id_cli)
    cli.nom_cli=nom_cli
    cli.apell_cli=apell_cli
    cli.tel_cli=tel_cli
    cli.tel_cli=tel_cli
    cli.dir_cli=dir_cli
    cli.email_cli=email_cli
    cli.save()
    messages.success(request, '¡Cliente Actualizado!')
    return redirect('/clientes/')


 # CRUD PEDIDO   
    
def GestionarPedido(request):
    ListaPed=Pedido.objects.all()
    cliente=Cliente.objects.all()
    maquina=Maquina.objects.all()
    return render(request,'BaseDeDatos/GestionPedido.html',{'pedidos':ListaPed,'clientes':cliente,'maquinas':maquina})

def RegistrarPedido(request): 
    cod_ped=request.POST['cod']
    fecha_ped=request.POST['fecha']
    maquina=Maquina.objects.get(cod_maquina=request.POST['descrip'])
    precio = float(request.POST['precio'])
    cantidad = float(request.POST['cant'])
    observaciones=request.POST['observ']
    cliente =Cliente.objects.get(id_cli=request.POST['idcli'])
    
    total = precio * cantidad
       
    pedido=Pedido.objects.create(cod_ped=cod_ped,fecha_ped=fecha_ped,cod_maquina=maquina,
                                 precio=precio,cantidad=cantidad,total=total,observaciones=observaciones,id_cli=cliente)
    messages.success(request, '¡Pedido Registrado!')
    return redirect('/pedidos/')

def ELiminarped(request,cod_ped):
    pedi=Pedido.objects.get(cod_ped=cod_ped)
    pedi.delete()
    messages.success(request, '¡Pedido Eliminado!')
    return redirect('/pedidos/')

def editarped(resquest,cod_ped):
    pedi=Pedido.objects.get(cod_ped=cod_ped)
    return render(resquest, 'BaseDeDatos/edicionPedi.html',{'pedidos':pedi})

def edicionPedi(request,cod_ped):
    
    pedi=Pedido.objects.get(cod_ped=cod_ped)
    cod_ped=request.POST['cod']
    fecha_ped=request.POST['fecha']
    #descrip_maqui=request.POST['descrip']
    precio = float(request.POST['precio'])
    cantidad = float(request.POST['cant'])
    observaciones=request.POST['observ']
    
    
    
    if fecha_ped:
        pedi.fecha_ped = fecha_ped
        
    
    pedi.cantidad = cantidad
    pedi.precio = precio
    pedi.observaciones = observaciones
    
    pedi.total = cantidad * precio
    
    pedi.save()
    messages.success(request, '¡Pedido Actualizado!')
    return redirect('/pedidos/')
    

# CRUD ORDENES PROD

def ListarOrden(request):
    Lista_ordenes=Orden.objects.all()
    pedido=Pedido.objects.all()
    maquina=Maquina.objects.all()
    area= Area.objects.all()
    return render(request,'BaseDeDatos/GestionOrden.html',{'ordenes':Lista_ordenes,'pedidos':pedido,'maquinas':maquina,'areas':area})

def RegistrarOrden(request):
    cod_ord=request.POST['cod']
    fecha_entrega=request.POST.get('fecha')
    maquina=Maquina.objects.get(cod_maquina=request.POST['modelo'])
    cant=request.POST['cant']
    area=Area.objects.get(cod_area=request.POST['ruta'])
    remision_img=request.POST['remi']
    cod_ped= Pedido.objects.get(cod_ped=request.POST['codp'])
    
    orden=Orden.objects.create(cod_ord=cod_ord,fecha_entrega=fecha_entrega,cod_maquina=maquina,cant=cant,
                               cod_area=area,remision_img=remision_img,cod_ped=cod_ped)
    messages.success(request, '¡Orden Registrada!')
    return redirect('/ordenes/')

def EliminarOrd(request,cod_ord):
    ord=Orden.objects.get(cod_ord=cod_ord)
    ord.save()
    messages.success(request, '¡Orden Eliminada!')
    return redirect('/ordenes/')

def editarorden(request,cod_ord):
    ord=Orden.objects.get(cod_ord=cod_ord)
    return render(request, 'BaseDeDatos/edicionOrd.html',{'ordenes':ord})

def edicionOrden(request,cod_ord):
    
    ord=Orden.objects.get(cod_ord=cod_ord) 

    fecha_entrega=request.POST.get('fecha')
    mod_maquina=request.POST['modelo']
    cant=request.POST['cant']
    area_trabajo=request.POST['ruta']
    remision_img=request.POST['remi']
    
    if fecha_entrega:#al cargar el editar, se tiene que seleccionar una fecha o el campo queda vacio y lanza error
            #esta validacin impide que eso suceda
        ord.fecha_entrega=fecha_entrega
    
    ord.cant=cant
    ord.remision_img=remision_img
    ord.save()
    messages.success(request, '¡Orden Actualizada!')
    return redirect('/ordenes/')

#CRUD MAQUINA

def GestionarMaquina(request):
    ListaMaq=Maquina.objects.all()
    return render(request,'BaseDeDatos/GestionMaquina.html',{'maquinas':ListaMaq})
    
    
def RegistrarMaqui(request):
    cod_maquina=request.POST['cod']
    nom_maquina=request.POST['nom']
    tipo_maquina=request.POST['tipo']
    cant_component=request.POST['comp']
    imagen=request.FILES.get('foto')
    
    maquin=Maquina.objects.create(cod_maquina=cod_maquina,nom_maquina=nom_maquina,tipo_maquina=tipo_maquina,
                                  cant_component=cant_component,imagen=imagen)
    messages.success(request, '¡Maquina Registrada!')
    return redirect('/maquinas/')

def Eliminarmaqui(request,cod_maquina):
    maq=Maquina.objects.get(cod_maquina=cod_maquina)
    maq.delete()
    messages.success(request, '¡Maquina Eliminada!')
    return redirect('/maquinas/')

def editarmaqui(request,cod_maquina):
    maq=Maquina.objects.get(cod_maquina=cod_maquina)
    return render(request, 'BaseDeDatos/edicionMaq.html',{'maquinas':maq})

def edicionMaqui(request,cod_maquina):
    
    maq=Maquina.objects.get(cod_maquina=cod_maquina)
    
    nom_maquina=request.POST['nom']
    tipo_maquina=request.POST['tipo']
    cant_component=request.POST['comp']
    imagen=request.FILES.get('foto')
    
    if imagen:
        maq.imagen=imagen
        
    maq.nom_maquina=nom_maquina
    maq.tipo_maquina=tipo_maquina
    maq.cant_component=cant_component

    maq.save()
    
    messages.success(request, '¡Maquina Actualizada!')
    return redirect('/maquinas/')

#CRUD AREA
def GestionaARea(request):
    ListaAreas=Area.objects.all()
    return render(request,'BaseDeDatos/GestionArea.html',{'areas':ListaAreas})

def RegistrarArea(request):
    cod_area=request.POST['cod']
    nombre=request.POST['nom']
    email_area=request.POST['email']
    
    area=Area.objects.create(cod_area=cod_area,nombre=nombre,email_area=email_area)
    messages.success(request, '¡Area Creada Exitosamente!')   
    return redirect('/areas/') 

def Eliminararea(request,cod_area):
    area=Area.objects.get(cod_area=cod_area)
    area.delete()
    messages.success(request, '¡Area Eliminada!')
    return redirect('/areas/')

def editarare(request,cod_area):
    area=Area.objects.get(cod_area=cod_area)
    return render(request,'BaseDeDatos/edicionArea.html',{'areas':area})

def edicionArea(request):
    cod_area=request.POST['cod']
    nombre=request.POST['nom']
    email_area=request.POST['email']
    
    area=Area.objects.get(cod_area=cod_area)
    area.nombre=nombre
    area.email_area=email_area
    area.save()
    messages.success(request, '¡Area Actualizada!')
    return redirect('/areas/')

# CRUD PIEZA
def GestionPieza(request):
    ListaPiez=Pieza.objects.all()
    maquina=Maquina.objects.all()
    return render(request,'BaseDeDatos/GestionPiez.html',{'piezas':ListaPiez,'maquinas':maquina})

def RegistrarPieza(request):
     
    cod_pieza=request.POST['cod']
    nom_pieza=request.POST['nom']
    tipo_material=request.POST['tipo']
    stock=request.POST['stok']
    maquina =Maquina.objects.get(cod_maquina=request.POST['cod_maquina'])
    
    pieza=Pieza.objects.create(cod_pieza=cod_pieza,nom_pieza=nom_pieza,
                               tipo_material=tipo_material,stock=stock,cod_maquina=maquina
                               )
    messages.success(request, '¡Pieza Registrada!')
    return redirect('/piezas/')

def EliminarPieza(request,cod_pieza):
    pieza=Pieza.objects.get(cod_pieza=cod_pieza)
    pieza.delete()
    messages.success(request, '¡Pieza Eliminada!')
    return redirect('/piezas/')

def editarpie(request,cod_pieza):
    pieza=Pieza.objects.get(cod_pieza=cod_pieza)
    return render(request,'BaseDeDatos/edicionPiez.html',{'piezas':pieza})
    

def edicionPieza(request):
    cod_pieza=request.POST['cod']
    nom_pieza=request.POST['nom']
    tipo_material=request.POST['tipo']
    stock=request.POST['stok']
    
    pieza=Pieza.objects.get(cod_pieza=cod_pieza)
    pieza.nom_pieza=nom_pieza
    pieza.tipo_material=tipo_material
    pieza.stock=stock
    pieza.save()
    messages.success(request, '¡Pieza Actualizada!')
    return redirect('/piezas/')

#Consulta de Cliente-Pedido
def ListaClientes_pedidos(request):
    pedido=Pedido.objects.all()
    return render(request, 'BaseDeDatos/Listacliente_pedido.html',{'pedidos': pedido})

class ListclienteListView(ListView):
    model=Pedido
    template_name='BaseDeDatos/Listacliente_pedido.html'
    context_object_name='pedidos'
#Convertir a pdf  
class ListclientePDF(View):
    
    def get(self,request,*args, **kwargs):
        pedido=Pedido.objects.all()
        data= {
            'pedidos':pedido
        }
        pdf= render_to_pdf('BaseDeDatos/Listacliente_pedido.html',data)
        return HttpResponse(pdf, content_type= 'application/pdf')
    
#Consulta Orden de produccion
    
def ordenProduccion(request,cod_ord):
    ord=Orden.objects.get(cod_ord=cod_ord)
    listOrd=Orden.objects.all()
    return render(request, 'BaseDeDatos/orden_produ.html',{'ordenes':ord,'listado':listOrd})

class ListOrdenListView(ListView):
    model=Orden
    template_name='BaseDeDatos/orden_produ.html'
    context_object_name='listado'
#Convertir a pdf     
class ListordenPDF(View):
    
    def get(self,request,*args, **kwargs):
        orden=Orden.objects.all()
        data= {
            'listado':orden
        }
        pdf= render_to_pdf('BaseDeDatos/orden_produ.html',data)
        return HttpResponse(pdf, content_type= 'application/pdf')
    
    







