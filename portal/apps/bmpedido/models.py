from django.db import models
from django.contrib.auth.models import User
from sqlserver_ado.models.manager import RawStoredProcedureManager
import datetime


#from django.contrib.auth.models import User
#from django.db import connection
# Create your models here.

#class Pedidos(models.Model):  
    # fields  
 #   url = models.CharField(max_length=900)  
  #  content = models.TextField()  
   # title = models.TextField()  
  
    # static method to perform a fulltext search  
    #@staticmethod  
    #def getValidarPedido(numeropedido):  
        # create a cursor  
     #   cur = connection.cursor()  
        # execute the stored procedure passing in   
        # search_string as a parameter  
      #  cur.callproc('[dbo].[WEB_GetValidaPedido]', [numeropedido])  
        # grab the results  
       # results = cur.fetchall()  
        #cur.close()  
  
        # wrap the results up into Document domain objects   
        #return [Pedidos(*row) for row in results]
 
  
class dolar(models.Model):        
    fecha = models.DateField(null=False, blank=False,db_column='fecha',primary_key=True,default=datetime.date.today())   
    compra = models.DecimalField(default = 0.000,null=False, blank=False,max_digits=6, db_column='compra',decimal_places=3)
    venta = models.DecimalField(default = 0.000,null=False, blank=False,max_digits=6, db_column='venta',decimal_places=3)
    created     = models.DateTimeField(auto_now_add = True,editable=False)
    updated     = models.DateTimeField(auto_now = True,editable=False)
    #created_by = models.CharField(max_length=50)
    #created_by = models.ForeignKey(User)
    
    class Meta:
        db_table = 'dolar'
    
    #def save(self):
        #if not self.created_by:
        #    self.created = datetime.date.today()
        #self.updated = datetime.datetime.today()
        #super(dolar, self).save()
              
class AsUsuarios(models.Model):
    usu_codigo = models.CharField(max_length=10, primary_key=True)    
    usu_nomb = models.CharField(max_length=40, db_column='Usu_Nomb', blank=True) # Field name made lowercase.    
    usu_estado = models.CharField(max_length=1, db_column='Usu_Estado', blank=True) # Field name made lowercase.
 
    class Meta:
        db_table = 'AS_USUARIOS'        
        


class VcaUnid(models.Model):
    unid_codi = models.CharField(max_length=3)
    unid_nomb = models.CharField(max_length=20)
    unid_medi = models.DecimalField(null=True, max_digits=6, decimal_places=3, blank=True)
    unid_desc = models.CharField(max_length=80)
    unid_imp = models.CharField(max_length=10, blank=True)
    nomb_corto = models.CharField(max_length=20, blank=True)
    tcodsunat = models.CharField(max_length=5, db_column='tCodSunat', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'vca_unid'
    def __unicode__(self):
        return self.unid_nomb

class VcaItem(models.Model):
    item_codi = models.CharField(max_length=12, primary_key=True)
    item_codcomer = models.CharField(max_length=50, blank=True)
    item_nomb = models.CharField(max_length=150, db_column='item_nomb', blank=True) # Field name made lowercase.
    unid_codi = models.CharField(max_length=50, db_column='unid_codi', blank=True) # Field name made lowercase.
    tunid = models.CharField(max_length=50, blank=True)
    vcaunid = models.ForeignKey(VcaUnid)
    class Meta:
        db_table = 'vca_item'
    def __unicode__(self):
        return self.item_nomb


class VcaOrpe(models.Model):
    
    orpe_serie = models.CharField(max_length=4, blank=True)
    orpe_nudo = models.CharField(max_length=10, blank=True)
    orpe_nume = models.CharField(max_length=14, primary_key=True)
    orpe_fech = models.DateTimeField(null=True, blank=True)
    prov_codi = models.CharField(max_length=11, blank=True)
    orpe_mone = models.CharField(max_length=1, blank=True)
    orpe_tica = models.TextField(blank=True) # This field type is a guess.
    orpe_feve = models.DateTimeField(null=True, blank=True)
    orpe_soli = models.CharField(max_length=3, blank=True)
    orpe_obse = models.CharField(max_length=800, blank=True)
    orpe_stat = models.CharField(max_length=1, blank=True)
    cod_iso = models.CharField(max_length=15, blank=True)
    dep_codi = models.CharField(max_length=3, blank=True)
    dap_codi = models.CharField(max_length=8, blank=True)
    usu_clave = models.CharField(max_length=6, blank=True)
    ceco_codi = models.CharField(max_length=6, blank=True)
    ceco_codi2 = models.CharField(max_length=6, blank=True)
    orpe_stat2 = models.CharField(max_length=1, blank=True)
    orpe_codi = models.CharField(max_length=10, blank=True)
    proy_nume = models.CharField(max_length=10, blank=True)
    alma_codi = models.CharField(max_length=3, blank=True)
    grup_codi = models.CharField(max_length=3, blank=True)
    empresa = models.DecimalField(max_digits=18, decimal_places=0)
    orpe_prio = models.CharField(max_length=1, blank=True)
    orpe_feent = models.DateTimeField(null=True, blank=True)
    lnego = models.CharField(max_length=2, blank=True)
    orpe_nure = models.CharField(max_length=50, blank=True)
    area_codi = models.CharField(max_length=3, blank=True)
    resp_codi = models.CharField(max_length=5, blank=True)
    userverificar = models.CharField(max_length=3, db_column='UserVerificar', blank=True) # Field name made lowercase.
    useraprobar = models.CharField(max_length=3, db_column='UserAprobar', blank=True) # Field name made lowercase.
    fverificar = models.DateTimeField(null=True, db_column='FVerificar', blank=True) # Field name made lowercase.
    faprobar = models.DateTimeField(null=True, db_column='FAprobar', blank=True) # Field name made lowercase.
    useranular = models.CharField(max_length=3, db_column='UserAnular', blank=True) # Field name made lowercase.
    fanular = models.DateTimeField(null=True, db_column='FAnular', blank=True) # Field name made lowercase.
    fimpointerfaz = models.DateTimeField(null=True, db_column='fImpoInterfaz', blank=True) # Field name made lowercase.
    ttipo = models.CharField(max_length=1, db_column='tTipo', blank=True) # Field name made lowercase.
    tnotificacion = models.CharField(max_length=1, db_column='tNotificacion', blank=True) # Field name made lowercase.
    ncantnotif = models.IntegerField(null=True, db_column='nCantNotif', blank=True) # Field name made lowercase.
    tmotivo = models.CharField(max_length=100, db_column='tMotivo', blank=True) # Field name made lowercase.
    fcierreauto = models.DateTimeField(null=True, db_column='fCierreAuto', blank=True) # Field name made lowercase.
    freprogramacion = models.DateTimeField(null=True, db_column='fReprogramacion', blank=True) # Field name made lowercase.
    treprogramacionuser = models.CharField(max_length=3, db_column='tReprogramacionUser', blank=True) # Field name made lowercase.
    nreprogramacion = models.IntegerField(null=True, db_column='nReprogramacion', blank=True) # Field name made lowercase.
    freprogramacionaprob = models.DateTimeField(null=True, db_column='fReprogramacionAprob', blank=True) # Field name made lowercase.
    treprogramacionaprobuser = models.CharField(max_length=3, db_column='tReprogramacionAprobUser', blank=True) # Field name made lowercase.
    objects = RawStoredProcedureManager()   
    
    class Meta:
        db_table = 'vca_orpe'
    
    def __unicode__(self):
        return self.orpe_nume

class VcaAlma(models.Model):
    alma_codi = models.CharField(max_length=3)
    alma_nomb = models.CharField(max_length=50, blank=True)
    alma_tipo = models.CharField(max_length=1, blank=True)
    plnc_cuen = models.CharField(max_length=8, blank=True)
    alma_ancho = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    alma_alto = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    alma_largo = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    alma_dir = models.CharField(max_length=70, blank=True)
    alma_negativo = models.CharField(max_length=1, blank=True)
    alma_abr = models.CharField(max_length=2, blank=True)
    alma_default = models.CharField(max_length=1, blank=True)
    sucu_codi = models.CharField(max_length=3, blank=True)
    ceco_codi = models.CharField(max_length=10, blank=True)
    alma_costo = models.IntegerField(null=True, blank=True)
    empresa = models.DecimalField(max_digits=18, decimal_places=0)
    alma_barra = models.IntegerField(null=True, blank=True)
    desp_pedido = models.IntegerField(null=True, blank=True)
    alma_pedido = models.CharField(max_length=3, blank=True)
    lnego = models.CharField(max_length=2, blank=True)
    alma_stat = models.CharField(max_length=1, blank=True)
    alma_oc = models.IntegerField(null=True, blank=True)
    alma_perecibles = models.IntegerField(null=True, blank=True)
    alma_invent = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'vca_alma'
        
class VcaOrped(models.Model):
    orpe_nume = models.CharField(max_length=14, primary_key=True)
    item_codi = models.CharField(max_length=12)    
    orpe_cant = models.TextField(blank=True) # This field type is a guess.
    tiop_codi = models.CharField(max_length=7, blank=True)
    unid_codi = models.CharField(max_length=3, blank=True)
    orpe_marca = models.CharField(max_length=10, blank=True)
    prov_codi = models.CharField(max_length=11, blank=True)
    ceco_codi = models.CharField(max_length=6, blank=True)
    orpe_fere = models.DateTimeField(null=True, blank=True)
    orpe_obse = models.CharField(max_length=120, blank=True)
    orpe_caan = models.TextField(blank=True) # This field type is a guess.
    orpe_prio = models.CharField(max_length=1, blank=True)
    orpe_carac = models.CharField(max_length=50, blank=True)
    orpe_sw = models.CharField(max_length=1, blank=True)
    sucu_codi = models.CharField(max_length=3, blank=True)
    empresa = models.DecimalField(max_digits=18, decimal_places=0)
    orpe_cantped = models.TextField(blank=True) # This field type is a guess.
    orpe_indice = models.IntegerField(primary_key=True)
    orpe_unidades = models.TextField(blank=True) # This field type is a guess.
    item_equi = models.TextField(blank=True) # This field type is a guess.
    item_fact_kilos = models.IntegerField(null=True, blank=True)
    item_fact_dual = models.CharField(max_length=1, blank=True)
    orpe_unidades_ent = models.TextField(blank=True) # This field type is a guess.
    orpe_feent = models.DateTimeField(null=True, blank=True)
    cobra_codi = models.CharField(max_length=3, blank=True)
    unid_kardex = models.CharField(max_length=3, blank=True)
    orpe_stat = models.CharField(max_length=1, blank=True)
    stock_act = models.TextField(blank=True) # This field type is a guess.
    item_exoigv = models.CharField(max_length=1, blank=True)
    orpe_prec = models.DecimalField(null=True, max_digits=18, decimal_places=2, blank=True)
    orpe_total = models.DecimalField(null=True, max_digits=18, decimal_places=2, blank=True)
    tdescripcion = models.CharField(max_length=4000, db_column='tDescripcion', blank=True) # Field name made lowercase.
    tcaracteristicas = models.CharField(max_length=4000, db_column='tCaracteristicas', blank=True) # Field name made lowercase.
    tmarcas = models.CharField(max_length=4000, db_column='tMarcas', blank=True) # Field name made lowercase.
    nvalerror = models.IntegerField(null=True, db_column='nValError', blank=True) # Field name made lowercase.
    fvalentregauser01 = models.DateTimeField(null=True, db_column='fValEntregaUser01', blank=True) # Field name made lowercase.
    fvalentregauser02 = models.DateTimeField(null=True, db_column='fValEntregaUser02', blank=True) # Field name made lowercase.
    faprobar = models.DateTimeField(null=True, db_column='fAprobar', blank=True) # Field name made lowercase.
    tobs = models.CharField(max_length=100, db_column='tObs', blank=True) # Field name made lowercase.
    fvalentregauserverif = models.DateTimeField(null=True, db_column='fValEntregaUserVerif', blank=True) # Field name made lowercase.
    nrepoauto = models.IntegerField(null=True, db_column='nRepoAuto', blank=True) # Field name made lowercase.
    neconomato = models.IntegerField(null=True, db_column='nEconomato', blank=True) # Field name made lowercase.
    fvalidacionprio = models.DateTimeField(null=True, db_column='fValidacionPrio', blank=True) # Field name made lowercase.
    fdespacho = models.DateTimeField(null=True, db_column='fDespacho', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'vca_orped'


class VcaOc(models.Model):
    oc_nume = models.CharField(max_length=20 ,primary_key=True ,blank=False)
    oc_soli = models.CharField(max_length=35, blank=True)
    oc_fech = models.DateTimeField()
    prov_codi = models.CharField(max_length=11)
    oc_cond = models.CharField(max_length=1, blank=True)
    cond_codi = models.CharField(max_length=3, blank=True)
    oc_feve = models.DateTimeField(null=True, blank=True)
    oc_mone = models.CharField(max_length=1)
    oc_tica = models.FloatField()
    cc_codi = models.CharField(max_length=6, blank=True)
    oc_obse = models.CharField(max_length=8000, blank=True)
    oc_igv = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    oc_igvd = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    oc_total = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    oc_totald = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    comp_codi = models.CharField(max_length=3, blank=True)
    oc_cc = models.CharField(max_length=6, blank=True)
    oc_fax = models.CharField(max_length=35, blank=True)
    oc_condi = models.CharField(max_length=50, blank=True)
    oc_nupe = models.CharField(max_length=7, blank=True)
    oc_flete = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    oc_segu = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    oc_toimpo = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    oc_fleted = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    oc_segud = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    oc_toimpod = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    oc_docproy = models.CharField(max_length=1, blank=True)
    oc_nudproy = models.CharField(max_length=20, blank=True)
    oc_tipo = models.CharField(max_length=2, blank=True)
    oc_impo = models.CharField(max_length=1, blank=True)
    req_nume = models.CharField(max_length=100, blank=True)
    copr_nume = models.CharField(max_length=7, blank=True)
    oc_confstat = models.CharField(max_length=1, blank=True)
    oc_obsserv = models.TextField(blank=True)
    orpe_nume = models.CharField(max_length=10, blank=True)
    oc_feent = models.DateTimeField(null=True, blank=True)
    oc_swigv = models.CharField(max_length=1, blank=True)
    usu_clave = models.CharField(max_length=6)
    alma_codi = models.CharField(max_length=3, blank=True)
    grup_codi = models.CharField(max_length=3, blank=True)
    cod_puerto = models.CharField(max_length=12, blank=True)
    cont_codi = models.CharField(max_length=5, blank=True)
    oc_codalt = models.CharField(max_length=12, blank=True)
    navi_codi = models.CharField(max_length=5, blank=True)
    conte_codi = models.CharField(max_length=5, blank=True)
    cod_puerto2 = models.CharField(max_length=10, blank=True)
    oc_fechaent = models.DateTimeField(null=True, blank=True)
    impo_envi = models.CharField(max_length=100, blank=True)
    oc_swimp = models.CharField(max_length=1, blank=True)
    oc_factpro = models.CharField(max_length=25, blank=True)
    ceco_codi = models.CharField(max_length=6, db_column='CECO_CODI', blank=True) # Field name made lowercase.
    sucu_codi = models.CharField(max_length=3, blank=True)
    empresa = models.DecimalField(max_digits=18, decimal_places=0)
    oc_tipoent = models.CharField(max_length=1, blank=True)
    oc_req = models.CharField(max_length=1, blank=True)
    dire_codi = models.CharField(max_length=3, blank=True)
    usercreate = models.CharField(max_length=3, db_column='UserCreate', blank=True) # Field name made lowercase.
    usermodified = models.CharField(max_length=3, db_column='UserModified', blank=True) # Field name made lowercase.
    useranular = models.CharField(max_length=3, db_column='UserAnular', blank=True) # Field name made lowercase.
    fcreate = models.DateTimeField(null=True, db_column='FCreate', blank=True) # Field name made lowercase.
    fmodified = models.DateTimeField(null=True, db_column='FModified', blank=True) # Field name made lowercase.
    fanular = models.DateTimeField(null=True, db_column='FAnular', blank=True) # Field name made lowercase.
    porc_percep = models.DecimalField(null=True, max_digits=19, decimal_places=4, blank=True)
    monto_perc = models.DecimalField(null=True, max_digits=19, decimal_places=4, blank=True)
    userverificar = models.CharField(max_length=3, db_column='UserVerificar', blank=True) # Field name made lowercase.
    fverificar = models.DateTimeField(null=True, db_column='FVerificar', blank=True) # Field name made lowercase.
    faprobacion = models.DateTimeField(null=True, db_column='FAprobacion', blank=True) # Field name made lowercase.
    oc_print = models.SmallIntegerField(null=True, blank=True)
    moti_codi = models.IntegerField(null=True, blank=True)
    tconfactura = models.CharField(max_length=1, db_column='tConFactura', blank=True) # Field name made lowercase.
    tmetodo = models.CharField(max_length=50, db_column='tMetodo', blank=True) # Field name made lowercase.
    ttermino = models.CharField(max_length=50, db_column='tTermino', blank=True) # Field name made lowercase.
    ttiempo = models.CharField(max_length=50, db_column='tTiempo', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'vca_oc'

class VcaOcdet(models.Model):
    oc_nume = models.CharField(max_length=20)
    item_codi = models.CharField(max_length=12)
    ocdet_cant = models.DecimalField(max_digits=12, decimal_places=3)
    ocdet_prec = models.DecimalField(max_digits=12, decimal_places=6)
    ocdet_des1 = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_des2 = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_suto = models.DecimalField(max_digits=12, decimal_places=3)
    ocdet_precd = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    ocdet_des1d = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_des2d = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_sutod = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_stock = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    ocdet_unidad = models.CharField(max_length=3)
    ocdet_cant_rec = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_fob = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_tofo = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_flete = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_segu = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_toimpo = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_igv = models.DecimalField(max_digits=12, decimal_places=3)
    orpe_nume = models.CharField(max_length=140, blank=True)
    ocdet_carac = models.CharField(max_length=50, blank=True)
    ocdet_prmi = models.DecimalField(null=True, max_digits=19, decimal_places=4, blank=True)
    ocdet_porc = models.DecimalField(null=True, max_digits=19, decimal_places=4, blank=True)
    req_nume = models.CharField(max_length=10, blank=True)
    oc_codalt = models.CharField(max_length=12, blank=True)
    ocdet_cont = models.CharField(max_length=5)
    ocdet_tipo = models.CharField(max_length=3)
    ocdet_foc = models.CharField(max_length=2)
    ceco_codi = models.CharField(max_length=6, blank=True)
    item_exoigv = models.CharField(max_length=1, blank=True)
    ocdet_unid_compra = models.CharField(max_length=2, blank=True)
    ocdet_cant_compra = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_cant_rec_compra = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_prec_compra = models.DecimalField(null=True, max_digits=12, decimal_places=6, blank=True)
    ocdet_suto_compra = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_precd_compra = models.DecimalField(null=True, max_digits=12, decimal_places=4, blank=True)
    ocdet_sutod_compra = models.DecimalField(null=True, max_digits=12, decimal_places=3, blank=True)
    ocdet_equival = models.DecimalField(null=True, max_digits=18, decimal_places=4, blank=True)
    sucu_codi = models.CharField(max_length=3, blank=True)
    oc_porc = models.DecimalField(null=True, max_digits=20, decimal_places=4, blank=True)
    empresa = models.DecimalField(max_digits=18, decimal_places=0)
    ocdet_item = models.CharField(max_length=8000, blank=True)
    ocdet_stat = models.CharField(max_length=1, blank=True)
    ocdet_cant_comp_impo = models.DecimalField(max_digits=18, decimal_places=3)
    ocdet_stat_impo = models.CharField(max_length=1, blank=True)
    ocdet_indice = models.IntegerField()
    ocdet_feent = models.DateTimeField(null=True, blank=True)
    ocdet_progent = models.IntegerField(null=True, blank=True)
    ocdet_unidades = models.DecimalField(null=True, max_digits=19, decimal_places=4, blank=True)
    item_fact_dual = models.CharField(max_length=1, blank=True)
    item_fact_kilos = models.IntegerField(null=True, blank=True)
    ocdet_unidades_rec = models.DecimalField(null=True, max_digits=19, decimal_places=4, blank=True)
    unid_desp = models.CharField(max_length=3, blank=True)
    ocdet_fdesp = models.DecimalField(null=True, max_digits=19, decimal_places=4, blank=True)
    indice = models.IntegerField(null=True, blank=True)
    item_perc = models.SmallIntegerField(null=True, blank=True)
    porc_percep = models.DecimalField(null=True, max_digits=19, decimal_places=4, blank=True)
    class Meta:
        db_table = 'vca_ocdet'
