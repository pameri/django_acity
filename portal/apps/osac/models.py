from django.db import models
 
from django.contrib.auth.models import User
# Create your models here.


class Osac(models.Model):
    fticket = models.DateTimeField(null=True, db_column='fTicket', blank=True) # Field name made lowercase.
    iduser = models.CharField(max_length=50, db_column='idUser', blank=True) # Field name made lowercase.
    idtipoticket = models.IntegerField(null=True, db_column='idTipoTicket', blank=True) # Field name made lowercase.
    testado = models.CharField(max_length=1, db_column='tEstado', blank=True) # Field name made lowercase.
    tprioridad = models.CharField(max_length=1, db_column='tPrioridad', blank=True) # Field name made lowercase.
    idservicio = models.IntegerField(null=True, db_column='idServicio', blank=True) # Field name made lowercase.
    tasunto = models.CharField(max_length=250, db_column='tAsunto', blank=True) # Field name made lowercase.
    tdescripcion = models.TextField(db_column='tDescripcion', blank=True) # Field name made lowercase. This field type is a guess.
    iduserrecepcion = models.CharField(max_length=50, db_column='idUserRecepcion', blank=True) # Field name made lowercase.
    frecepcion = models.CharField(max_length=10, db_column='fRecepcion', blank=True) # Field name made lowercase.
    idusercierre = models.CharField(max_length=50, db_column='idUserCierre', blank=True) # Field name made lowercase.
    fcierre = models.DateTimeField(null=True, db_column='fCierre', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'Ticket'
        
    def __unicode__(self):
        return self.tasunto
    


        