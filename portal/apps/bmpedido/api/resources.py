from tastypie.resources import ModelResource
from portal.apps.bmpedido.models import VcaItem ,VcaUnid
from tastypie.serializers import Serializer
from tastypie import fields

class VcaUnidResource(ModelResource):
    class Meta:
        queryset = VcaUnid.objects.all()
        resource_name = 'unid_codi'
        
class ProductoResource(ModelResource):
    #unid_codi = fields.ForeignKey(VcaUnidResource, 'vcaunid', null=True, blank=True) 
    #'path.to.api.resources.AuthorResource', 'author_set', related_name='entry'
    
    #user = fields.ForeignKey(UserResource, 'user', fields = ['name', date_of_birth', ])
    class Meta:
        resource_name = 'item'
        queryset = VcaItem.objects.all()
        allowed_methods = ['get']          
        #serializer = Serializer(formats=['json', 'plist','xml'])
        serializer = Serializer(formats=['json', 'jsonp', 'xml', 'yaml', 'html', 'plist'])
        #fields = ['item_codcomer', 'item_nomb']  