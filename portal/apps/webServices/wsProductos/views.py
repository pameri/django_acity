# Create your views here.
from django.http import HttpResponse
from portal.apps.bmpedido.models import VcaItem
# Integramos la serializacion de los objetos
from django.core import serializers



def wsProductos_view(request):
	data = serializers.serialize("json",VcaItem.objects.all())
	# Retorna la informacion en formato json
	return HttpResponse(data,mimetype='application/json')