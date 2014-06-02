from django.conf.urls import patterns,url


urlpatterns = patterns('portal.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	#url(r'^lista/$','listado_tickets_view',name='vista_listado_tickets'),	
	#url(r'^about/$','about_view',name='vista_about'),
	#url(r'^tickets/page/(?P<pagina>.*)/$','tickets_view',name='vista_ticket'),	
	#url(r'^ticket/(?P<id_prod>.*)/$','singleTicket_view',name='vista_single_ticket'),
	#url(r'^contacto/$','contacto_view',name='vista_contacto'),
	#url(r'^gestionticket/$','index_ticket_view',name='vista_principal_ticket'),
	#url(r'^formticket/$','manage_tickets',name='vista_form_ticket'),
	#url(r'^login/$','login_view',name='vista_login'),
	#url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'home/login.html'}),
	url(r'^logout/$','logout_view',name='vista_logout'),
)
urlpatterns += patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'home/login.html'},name = 'vista_login'),
)
urlpatterns += patterns('portal.apps.bmpedido.views',
	url(r'^tipocambio/page/(?P<pagina>.*)/$','tipocambio_view',name='vista_tipocambio'),	
	url(r'^pedidos/page/(?P<pagina>.*)/$','pedidos_view',name='vista_pedido'),	
	url(r'^pedidos/pagev/(?P<pagina>.*)/$','pedidosverificar_view',name='vista_pedido'),
	url(r'^pedidos/pagen/(?P<pagina>.*)/$','pedidosanular_view',name='vista_pedido_anular'),
	url(r'^ocaprobar/page/(?P<pagina>.*)/$','ocaprobar_view',name='vista_ocaprobar'),
	url(r'^ocverificar/page/(?P<pagina>.*)/$','ocverificar_view',name='vista_ocverificar'),
	url(r'^ocanular/page/(?P<pagina>.*)/$','ocanular_view',name='vista_ocanular'),
	url(r'^estadistica/$','estadisticas',name='vista_estadistica'),
	url(r'^tutorial/$','tutorial_view',name='vista_pdf'),								
)

