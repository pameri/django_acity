from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from portal.apps.bmpedido.api.resources import ProductoResource,VcaUnidResource


producto_resource = ProductoResource()

v1_api = Api(api_name='v1')
v1_api.register(VcaUnidResource())
v1_api.register(ProductoResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^portal/', include('portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^',include('portal.apps.home.urls')),
    url(r'^',include('portal.apps.blog.urls')),
    url(r'^',include('portal.apps.bmpedido.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^api/', include(v1_api.urls)),    
    #url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^',include('portal.apps.webServices.wsProductos.urls')),
    url(r'^',include('portal.apps.webServices.wsPedidoDetalles.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),    
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    
    
    #url(r'^static/(?P.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    
    
)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
    