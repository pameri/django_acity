# Create your views here.
from portal.apps.bmpedido.models import VcaOrpe,VcaOrped,AsUsuarios, VcaOc,VcaOcdet,dolar
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required,permission_required

from django.utils import simplejson
from django.http import HttpResponse
from portal.apps.bmpedido.forms import addTipoCambioForm
from django.http import HttpResponseRedirect
#import datetime
from datetime import *
from django.contrib.auth.models import User 
from django.db import connection,transaction
#from django.contrib.auth.models import User
import qsstats
from reportlab.pdfgen import canvas
import os

#def tutorial_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    #fname = '/media/pdf/TUTORIAL_MOVIL_BM.pdf'
    #response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'filename='+fname
    
    # Create the PDF object, using the response object as its "file."
    # p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    #p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    #p.showPage()
    #p.save()
    # return response
@login_required
#@permission_required('bmpedido.can_consultar', raise_exception=True)
def tipocambio_view(request,pagina):
    if request.user.has_perm('bmpedido.can_consultar'):     
        lista_tc = dolar.objects.all().order_by('-fecha') # Select * from ventas_productos where status = True
        paginator = Paginator(lista_tc,30) # Cuantos productos quieres por pagina? = 3
        try:
            page = int(pagina)
        except:
            page = 1
        try:
            tipocambio = paginator.page(page)
        except (EmptyPage,InvalidPage):
            tipocambio = paginator.page(paginator.num_pages)
        ctx = {'tipocambio':tipocambio}    
        return render_to_response('bmpedido/lista_tipocambio.html',ctx,context_instance=RequestContext(request))  
    else:
        ctx = {'informacion':'No tiene acceso a consultar tipo de cambio'}
        #return HttpResponse("No tiene acceso a ingresar tipo de cambio")
        return render_to_response('home/acceso_restringido.html',ctx,context_instance=RequestContext(request))    


@login_required 
def add_tipocambio_view(request):
    if request.user.has_perm('bmpedido.add_dolar'):        
        info = "Iniciado"
        info_enviado = False
        if request.method == "POST":
            form = addTipoCambioForm(request.POST,request.FILES)
            if form.is_valid():
                info_enviado = True
                add = form.save(commit=False)
                #add.status = True
                add.save() # Guardamos la informacion
                #form.save_m2m() # Guarda las relaciones de ManyToMany
                info = "Guardado satisfactoriamente"
                #return HttpResponseRedirect('/tipocambio/page/1/')
        else:
            form = addTipoCambioForm()
        ctx = {'form':form,'informacion':info,'info_enviado':info_enviado}
        return render_to_response('bmpedido/addTipoCambio.html',ctx,context_instance=RequestContext(request))
    else:
        ctx = {'informacion':'No tiene acceso a ingresar tipo de cambio'}
        #return HttpResponse("No tiene acceso a ingresar tipo de cambio")
        return render_to_response('home/acceso_restringido.html',ctx,context_instance=RequestContext(request)) 
         


def tutorial_view(request):  
    ruta = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'media/pdf/')
    fname = 'TUTORIAL_MOVIL_BM.pdf'  
    return printPdf(os.path.dirname(ruta+fname))

def printPdf(path):
    with open(path, "rb") as f:
        data = f.read()
    return HttpResponse(data, mimetype='application/pdf')
  
def estadisticas(request):

    GOOGLE_API_KEY = 'AIzaSyAQz45z6xJrAwMPHncF4vUgmbfGrCoHwGE'

    qs = User.objects.all()
    qss = qsstats.QuerySetStats(qs, 'date_joined')
    #hoy = datetime.date.today()
    #hace_2_semanas = hoy - datetime.timedelta(weeks=2)

    #users_stats = qss.time_series(hace_2_semanas, hoy)

    return render_to_response('bmpedido/estadisticas.html', locals(), context_instance=RequestContext(request))

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]



@login_required
def pedidos_view(request,pagina):
    if request.user.has_perm('bmpedido.can_consultar_pedido_aprobar'):            
        username = None
        if request.user.is_authenticated():
            #if 'admin' in request.user.username:
                #return HttpResponse("No tiene acceso a aprobar pedidos")
            username = request.user.username
            
        if request.method=="POST":
            if "pedido_id" in request.POST:
                try:
                    id_pedido = request.POST['pedido_id']
                    p = VcaOrpe.objects.get(orpe_nume=id_pedido)
                    pdetalle = VcaOrped.objects.filter(orpe_nume=id_pedido)
                    
                    #veriricar op                                
                    if p.orpe_stat != 'V' :
                        mensaje = {"status":p.orpe_stat,"pedido_id":p.orpe_nume}                    
                        return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                    #instancia la coneccion y cursor
                    cursor = connection.cursor()
                    #inicializamos                
                    try:
                        cursor.callproc('[dbo].[WEB_GetValidaPedido]', [id_pedido])
                        result_list = dictfetchall(cursor)
                        for r in result_list:
                            bvenc = r.values()
                        if bvenc ==[1]:
                            #pdetalle.update(orpe_feent=pdetalle.fvalentregauser01 )
                            cursor.execute("UPDATE vca_orped SET orpe_feent = fvalentregauser01 WHERE orpe_nume = %s", [id_pedido])
                            transaction.commit_unless_managed()
                            #mensaje = {"status":"1","pedido_id":p.orpe_nume}
                            #return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                    except:                    
                        mensaje = {"status":"1","pedido_id":p.orpe_nume}
                        return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                    finally:
                        cursor.close()              
                                     
                    p.orpe_stat = 'A'
                    p.proy_nume = 'w'
                    #p.faprobar = datetime.date.today() #datetime.today()
                    p.faprobar = datetime.today()
                    u = AsUsuarios.objects.get(usu_nomb=username)    
                    p.useraprobar = u.usu_codigo
                    
                    #p.delete() # Elinamos objeto de la base de datos
                    p.save() # actualizamos el estado del pedido o el objeto de la base de datos
                    
                    pdetalle.update(orpe_stat = 'A')
                    # actualizamos el detall del pedido o el objeto de la base de datos
                    
                    mensaje = {"status":"True","pedido_id":p.orpe_nume}
                    
                    return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                except:
                    mensaje = {"status":"False"}
                    return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')                
                
        cursor = connection.cursor()   
        try:
            cursor.callproc('[dbo].[WEB_ListadoPedido]', [username, 'V'])
            result_list = dictfetchall(cursor)
        finally:
            cursor.close()   
        
        paginator = Paginator(result_list,5) # Cuantos productos quieres por pagina? = 3
        #page = request.GET.get('pagina')    
        try:
            page = int(pagina)
        except:
            page = 1
                
        try:
            pedidos = paginator.page(page)
        except (EmptyPage,InvalidPage):
            pedidos = paginator.page(paginator.num_pages)    
        
        ctx = {'pedidos':pedidos}
        return render_to_response('bmpedido/pedidos.html',ctx,context_instance=RequestContext(request))
    else:
        ctx = {'informacion':'No tiene acceso a consultar pedidos por Aprobar'}
        #return HttpResponse("No tiene acceso a ingresar tipo de cambio")
        return render_to_response('home/acceso_restringido.html',ctx,context_instance=RequestContext(request))
        
    

@login_required
def pedidosverificar_view(request,pagina):
    if request.user.has_perm('bmpedido.can_consultar_pedido_verificar'):
            
        username = None
        if request.user.is_authenticated():
            username = request.user.username
            
        if request.method=="POST":
            if "pedido_id2" in request.POST:
                try:
                    id_pedido = request.POST['pedido_id2']
                    p = VcaOrpe.objects.get(orpe_nume=id_pedido)
                    pdetalle = VcaOrped.objects.filter(orpe_nume=id_pedido)
                    if p.orpe_stat != 'E' :
                        mensaje = {"status":p.orpe_stat,"pedido_id2":p.orpe_nume}                    
                        return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                    #instancia la coneccion y cursor
                    cursor = connection.cursor()
                    #inicializamos                
                    try:
                        cursor.callproc('[dbo].[WEB_GetValidaPedido]', [id_pedido])
                        result_list = dictfetchall(cursor)
                        for r in result_list:
                            bvenc = r.values()
                        if bvenc ==[1]:
                            cursor.execute("UPDATE vca_orped SET orpe_feent = fvalentregauser01 WHERE orpe_nume = %s", [id_pedido])
                            transaction.commit_unless_managed()
                            #mensaje = {"status":"1","pedido_id2":p.orpe_nume}
                            #return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                        
                    except:                    
                        mensaje = {"status":"1","pedido_id2":p.orpe_nume}
                        return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json') 
                    finally:
                        cursor.close()              
                    
                    p.orpe_stat = 'V'
                    p.proy_nume = 'X'
                    #p.fverificar =  datetime.date.today()#datetime.today()
                    p.fverificar =  datetime.today()
                    u = AsUsuarios.objects.get(usu_nomb =username )
                    p.userverificar = u.usu_codigo                
                    
                    #p.delete() # Elinamos objeto de la base de datos
                    p.save() # actualizamos el estado del pedido o el objeto de la base de datos
                    
                    pdetalle.update(orpe_stat = 'V')
                        
                    mensaje = {"status":"True","pedido_id2":p.orpe_nume}
                        
                    return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                except:
                    mensaje = {"status":"False"}
                    return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                
        cursor = connection.cursor()
        try:
            cursor.callproc('[dbo].[WEB_ListadoPedido]', [username, 'E'])
            #retorna lisado de datos para mostar en la vista
            result_list = dictfetchall(cursor)
        finally:
            cursor.close()
    
        paginator = Paginator(result_list,5) # Cuantos productos quieres por pagina? = 3        
        try:
            page = int(pagina)
        except:
            page = 1
                
        try:
            pedidos = paginator.page(page)
        except (EmptyPage,InvalidPage):
            pedidos = paginator.page(paginator.num_pages)
        
        ctx = {'pedidosVerificar':pedidos}
        return render_to_response('bmpedido/pedidoverificar.html',ctx,context_instance=RequestContext(request))
    else:
        ctx = {'informacion':'No tiene acceso a consultar pedidos por Verificar'}        
        return render_to_response('home/acceso_restringido.html',ctx,context_instance=RequestContext(request))
        


@login_required
def pedidosanular_view(request,pagina):
    if request.user.has_perm('bmpedido.can_consultar_pedido_anular'):
    
        username = None
        if request.user.is_authenticated():
            username = request.user.username
            
        if request.method=="POST":
            if "pedido_id" in request.POST:
                try:
                    id_pedido = request.POST['pedido_id']
                    p = VcaOrpe.objects.get(orpe_nume=id_pedido)
                    pdetalle = VcaOrped.objects.filter(orpe_nume=id_pedido)
                    if p.orpe_stat != 'A':
                        mensaje = {"status":p.orpe_stat,"pedido_id":p.orpe_nume}               
                        return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                   
                    p.orpe_stat = 'N'
                    #p.fanular =  datetime.date.today()#datetime.today()
                    p.fanular =  datetime.today()
                    u = AsUsuarios.objects.get(usu_nomb =username )
                    p.useranular = u.usu_codigo                
                    
                    #p.delete() # Elinamos objeto de la base de datos
                    p.save() # actualizamos el estado del pedido o el objeto de la base de datos
                    
                    pdetalle.update(orpe_stat = 'N')
                    
                    mensaje = {"status":"True","pedido_id":p.orpe_nume}                        
                    return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                except:
                    mensaje = {"status":"False"}
                    return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                
        cursor = connection.cursor()
        try:
            cursor.callproc('[dbo].[WEB_ListadoPedido]', [username, 'A'])
            #retorna lisado de datos para mostar en la vista
            result_list = dictfetchall(cursor)
        finally:
            cursor.close()
    
        paginator = Paginator(result_list,5) # Cuantos productos quieres por pagina? = 3        
        try:
            page = int(pagina)
        except:
            page = 1
                
        try:
            pedidos = paginator.page(page)
        except (EmptyPage,InvalidPage):
            pedidos = paginator.page(paginator.num_pages)
        
        ctx = {'pedidos':pedidos}
        return render_to_response('bmpedido/pedidoanular.html',ctx,context_instance=RequestContext(request))
    else:
        ctx = {'informacion':'No tiene acceso anular pedidos aprobados'}        
        return render_to_response('home/acceso_restringido.html',ctx,context_instance=RequestContext(request))


@login_required
def ocaprobar_view(request,pagina):
    if request.user.has_perm('bmpedido.can_consultar_oc_aprobar'):    
        username = None
        if request.user.is_authenticated():
            username = request.user.username
            
        if request.method=="POST":
            if "pedido_id" in request.POST:
                try:
                    id_pedido = request.POST['pedido_id']
                    p = VcaOc.objects.get(oc_nume=id_pedido)
                    pdetalle = VcaOcdet.objects.filter(oc_nume=id_pedido)
                    if p.oc_cond != 'V' :
                        mensaje = {"status":p.oc_cond,"pedido_id":p.oc_nume}                    
                        return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')    
                    p.oc_cond = 'A' 
                    #print  datetime.today()
                    p.faprobacion =  datetime.today()
                    u = AsUsuarios.objects.get(usu_nomb=username )    
                    p.oc_soli = u.usu_codigo
                    
                    #p.delete() # Elinamos objeto de la base de datos
                    p.save() # actualizamos el estado del pedido o el objeto de la base de datos
                    pdetalle.update(ocdet_stat = 'A') 
                    
                    mensaje = {"status":"True","pedido_id":p.oc_nume}                        
                    return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                except:
                    mensaje = {"status":"False"}
                    return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')             
    
                    
                
        cursor = connection.cursor()   
        try:
            cursor.callproc('[dbo].[WEB_Listado_oc]', [username, 'V'])
            result_list = dictfetchall(cursor)
        finally:
            cursor.close()   
        
        paginator = Paginator(result_list,5) # Cuantos productos quieres por pagina? = 3
        #page = request.GET.get('pagina')    
        try:
            page = int(pagina)
        except:
            page = 1
                
        try:
            pedidos = paginator.page(page)
        except (EmptyPage,InvalidPage):
            pedidos = paginator.page(paginator.num_pages)    
        
        ctx = {'pedidos':pedidos}
        return render_to_response('bmpedido/oc_aprobar.html',ctx,context_instance=RequestContext(request))
    else:
        ctx = {'informacion':'No tiene acceso aprobar ordenes de compra'}        
        return render_to_response('home/acceso_restringido.html',ctx,context_instance=RequestContext(request))

@login_required
def ocverificar_view(request,pagina):
    if request.user.has_perm('bmpedido.can_consultar_oc_verificar'):    
        username = None
        if request.user.is_authenticated():
            username = request.user.username
            
        if request.method=="POST":
            if "pedido_id" in request.POST:
                try:
                    id_pedido = request.POST['pedido_id']
                    p = VcaOc.objects.get(oc_nume=id_pedido)
                    pdetalle = VcaOcdet.objects.filter(oc_nume=id_pedido)
                    if p.oc_cond != 'E' :
                        mensaje = {"status":p.oc_cond,"pedido_id":p.oc_nume}                    
                        return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')                                
                    p.oc_cond = 'V' 
                    #print  datetime.today()
                    p.fverificar =  datetime.today()
                    u = AsUsuarios.objects.get(usu_nomb=username )    
                    p.userverificar = u.usu_codigo
                    
                    #p.delete() # Elinamos objeto de la base de datos
                    p.save() # actualizamos el estado del pedido o el objeto de la base de datos
                    
                    pdetalle.update(ocdet_stat = 'V') 
                    
                    mensaje = {"status":"True","pedido_id":p.oc_nume}                        
                    return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                except:
                    mensaje = {"status":"False"}
                    return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')                
                
        cursor = connection.cursor()   
        try:
            cursor.callproc('[dbo].[WEB_Listado_oc]', [username, 'E'])
            result_list = dictfetchall(cursor)
        finally:
            cursor.close()   
        
        paginator = Paginator(result_list,5) # Cuantos productos quieres por pagina? = 3
        #page = request.GET.get('pagina')    
        try:
            page = int(pagina)
        except:
            page = 1
                
        try:
            pedidos = paginator.page(page)
        except (EmptyPage,InvalidPage):
            pedidos = paginator.page(paginator.num_pages)    
        
        ctx = {'pedidos':pedidos}
        return render_to_response('bmpedido/oc_verificar.html',ctx,context_instance=RequestContext(request))
    else:
        ctx = {'informacion':'No tiene acceso a verificar ordenes de compra'}        
        return render_to_response('home/acceso_restringido.html',ctx,context_instance=RequestContext(request))

@login_required
def ocanular_view(request,pagina):
    if request.user.has_perm('bmpedido.can_consultar_oc_anular'):        
        username = None
        if request.user.is_authenticated():
            username = request.user.username
            
        if request.method=="POST":
            if "pedido_id" in request.POST:
                try:
                    id_pedido = request.POST['pedido_id']
                    p = VcaOc.objects.get(oc_nume=id_pedido)
                    pdetalle = VcaOcdet.objects.filter(oc_nume=id_pedido)
                    if p.oc_cond != 'A' :
                        mensaje = {"status":p.oc_cond ,"pedido_id":p.oc_nume}                    
                        return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')                
                    p.oc_cond = 'N'
                    #print  datetime.today()
                    p.fanular =  datetime.today()
                    u = AsUsuarios.objects.get(usu_nomb=username )    
                    p.useranular = u.usu_codigo
                    
                    #p.delete() # Elinamos objeto de la base de datos
                    p.save() # actualizamos el estado del pedido o el objeto de la base de datos
                    
                    pdetalle.update(ocdet_stat = 'N') 
                        
                    mensaje = {"status":"True","pedido_id":p.oc_nume}   
                    return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
                except:
                    mensaje = {"status":"False"}
                    return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')         
        cursor = connection.cursor()   
        try:
            cursor.callproc('[dbo].[WEB_Listado_oc]', [username, 'A'])
            result_list = dictfetchall(cursor)
        finally:
            cursor.close()   
        
        paginator = Paginator(result_list,5) # Cuantos productos quieres por pagina? = 3
        #page = request.GET.get('pagina')    
        try:
            page = int(pagina)
        except:
            page = 1
                
        try:
            pedidos = paginator.page(page)
        except (EmptyPage,InvalidPage):
            pedidos = paginator.page(paginator.num_pages)    
        
        ctx = {'pedidos':pedidos}
        return render_to_response('bmpedido/oc_anular.html',ctx,context_instance=RequestContext(request))
    else:
        ctx = {'informacion':'No tiene acceso anular ordenes de compra aprobadas'}        
        return render_to_response('home/acceso_restringido.html',ctx,context_instance=RequestContext(request))

