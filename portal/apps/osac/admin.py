from django.contrib import admin
#from osac.apps.home.models import userProfile

from portal.apps.osac.models import Ticket

class ticketAdmin(admin.ModelAdmin):
    list_display    = ['fticket','iduser','tasunto']
    ordering        = ['fticket']
    list_filter     = ['iduser']
    
admin.site.register(Ticket,ticketAdmin)

#admin.site.register(userProfile)
