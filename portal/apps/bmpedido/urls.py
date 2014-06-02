from django.conf.urls import patterns,url

urlpatterns = patterns('portal.apps.bmpedido.views',
					
	url(r'^add/tipocambio/$','add_tipocambio_view',name= "vista_agregar_tipocambio"),				
	#url(r'^$','main',name='vista_blog'),
	#url(r'^bmpedido/page/(?P<pagina>.*)/$','pedidos_view',name='vista_pedido'),
	#url(r'^bmpedido1/paginav/(?P<paginas>.*)/$','pedidosverificar_view',name='vista_pedido_verificar'),
	#url(r'^tickets/page/(?P<pagina>.*)/$','tickets_view',name='vista_ticket'),
	
)

