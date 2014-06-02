from django.conf.urls import patterns,url

urlpatterns = patterns('portal.apps.webServices.wsPedidoDetalles.views',
	url(r'^ws/pedidodetalles/(?P<codigo>.*)/$','wsPedidoDetalles_view',name= "ws_pedidodetalles_url"),
	url(r'^ws/pedidos/(?P<coduser>.*)/$','wsPedidos_view',name= "ws_pedidos_url"),
	url(r'^ws/ocdetalles/(?P<codigo>.*)/$','wsOCDetalles_view',name= "ws_ocdetalles_url"),
)