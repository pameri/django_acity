# Create your views here.
from django.http import HttpResponse
from portal.apps.bmpedido.models import VcaOrped,VcaItem
# Integramos la serializacion de los objetos
from django.core import serializers
from django.db import connection
import json , decimal



class ComplexEncoder(json.JSONEncoder):
	def default(self, obj):
		try:
			return super(ComplexEncoder, obj).default(obj)
		except TypeError:
			return str(obj)

def dictfetchall(cursor):
	#"Returns all rows from a cursor as a dict"
	desc = cursor.description
	return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def date_handler(obj):
	return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def wsPedidos_view(request,coduser):
	
	
	cursor = connection.cursor()
	#cursor.execute("select c.alma_codi as alma_codi,isnull(c.orpe_obse,'') as  orpe_obse ,d.id,d.orpe_nume,i.item_codcomer,i.item_nomb,convert(varchar(50),d.orpe_cant) as orpe_cant , u.unid_nomb as unidad,convert(varchar(10),d.orpe_feent,103) as fentrega from vca_orped  d inner join vca_item i on d.item_codi = i.item_codi join vca_unid u on u.unid_codi = i.unid_codi join vca_orpe c on c.orpe_nume = d.orpe_nume where d.orpe_nume = %s", [codigo])
	cursor.callproc('[dbo].[WEB_ListadoPedido]', [coduser, 'E'])
	#json_string = json.dumps(cursor.fetchall())
	#json_string = json.dumps(dict(cursor.fetchall()))
	
	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]	
	pedidos = []
	
	for row in rows:
		pedido = {}	
		
		for prop, val in zip(cols, row):
			pedido[prop] = val
		
		pedidos.append(pedido)	
	# Create a string representation of your array of songs.
	json_string = json.dumps(pedidos,default=date_handler)
	return HttpResponse(json_string,mimetype='application/json')



def wsPedidoDetalles_view(request,codigo):	
	cursor = connection.cursor()
	cursor.execute("select c.alma_codi as alma_codi,isnull(c.orpe_obse,'') as  orpe_obse,d.orpe_nume,i.item_codcomer,i.item_nomb,convert(varchar(50),d.orpe_cant) as orpe_cant , u.unid_nomb as unidad,convert(varchar(10),d.orpe_feent,103) as fentrega from vca_orped  d inner join vca_item i on d.item_codi = i.item_codi join vca_unid u on u.unid_codi = i.unid_codi join vca_orpe c on c.orpe_nume = d.orpe_nume where d.orpe_nume = %s", [codigo])
	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]	
	pedidos = []
	
	for row in rows:
		pedido = {}	
		
		for prop, val in zip(cols, row):
			pedido[prop] = val
		
		pedidos.append(pedido)	
	# Create a string representation of your array of songs.
	json_string = json.dumps(pedidos,default=date_handler)
	return HttpResponse(json_string,mimetype='application/json')


def decimal_default(obj):
	if isinstance(obj, decimal.Decimal):
		return float(obj)
	raise TypeError

		
def wsOCDetalles_view(request,codigo):	
	cursor = connection.cursor()
	cursor.execute("select c.alma_codi as alma_codi,isnull(c.oc_obse,'') as  oc_obse ,d.oc_nume,i.item_codcomer,i.item_nomb,d.ocdet_cant as ocdet_cant , case D.item_exoigv WHEN '1' THEN  round(D.ocdet_prec_compra,2) ELSE round(D.ocdet_prec_compra * (1+(D.ocdet_igv/100)),2)  END as precio,u.unid_nomb as unidad,convert(varchar(10),d.ocdet_feent,103) as fentrega,case D.item_exoigv WHEN '1' THEN  round(D.ocdet_prec_compra,2) ELSE round(D.ocdet_prec_compra * (1+(D.ocdet_igv/100)),2)  END  * d.ocdet_cant as subtotal from vca_ocdet  d inner join vca_item i on d.item_codi = i.item_codi join vca_unid u on u.unid_codi = d.ocdet_unid_compra join vca_oc c on c.oc_nume = d.oc_nume where d.oc_nume = %s order by d.ocdet_indice asc " , [codigo])
	rows = [x for x in cursor]
	cols = [x[0] for x in cursor.description]	
	pedidos = []
	
	for row in rows:
		pedido = {}	
		
		for prop, val in zip(cols, row):
			pedido[prop] = val
		
		pedidos.append(pedido)	
	# Create a string representation of your array of songs.
	json_string = json.dumps(pedidos,default=decimal_default)
	return HttpResponse(json_string,mimetype='application/json')

