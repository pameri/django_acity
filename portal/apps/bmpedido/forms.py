from django import forms
from django.forms import ModelForm, CharField, TextInput
from portal.apps.bmpedido.models import dolar
from django.contrib.admin import widgets 
from django.forms.extras.widgets import SelectDateWidget
#from django.contrib.admin.widgets import AdminDateWidget 


    
    
class addTipoCambioForm(forms.ModelForm):
    
    #fecha= forms.DateField()
    #fecha = forms.TimeField(widget=widgets.AdminTimeWidget)    
    fecha = forms.DateField(widget=SelectDateWidget() ,initial='count',)
    #fecha = forms.DateTimeField(widget=widgets.AdminDateWidget())
    class Meta:
        model   = dolar
        exclude = {'created','updated','created_by',} 
    
       
    #def __init__(self, *args, **kwargs):
        #super(addTipoCambioForm, self).__init__(*args, **kwargs)
        #self.fields['fecha'].widget = widgets.AdminDateWidget()        
        #self.fields['fecha'].widget = widgets.AdminSplitDateTime()
    def clean_venta(self):        
        diccionario_limpio = self.cleaned_data      
        venta = diccionario_limpio.get('venta')
        if venta <= 0:
            raise forms.ValidationError("El tipo de cambio de venta debe ser mayor a cero")
        
        elif venta < 2.5:            
            raise forms.ValidationError("El tipo de cambio de venta esta configurado entre 2.5 y 3.5")
        
        elif venta > 3.5:            
            raise forms.ValidationError("El tipo de cambio de venta esta configurado entre 2.5 y 3.5")
                
        return venta
    def clean_compra(self):        
        diccionario_limpio = self.cleaned_data      
        compra = diccionario_limpio.get('compra')
        if compra <= 0:
            raise forms.ValidationError("El tipo de cambio de compra debe ser mayor a cero")
        elif compra < 2.5:            
            raise forms.ValidationError("El tipo de cambio de compra esta configurado entre 2.5 y 3.5")
        
        elif compra > 3.5:            
            raise forms.ValidationError("El tipo de cambio de compra esta configurado entre 2.5 y 3.5")
        
        return compra
