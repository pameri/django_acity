from django.conf.urls import patterns,url


urlpatterns = patterns('portal.apps.blog.views',
	#url(r'^$','main',name='vista_blog'),
	url(r'^blog/$','main',name='vista_blog'),

)
