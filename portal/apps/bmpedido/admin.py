from django.contrib import admin
from portal.apps.bmpedido.models import dolar
#admin.site.register(userProfile)
class DolarAdmin(admin.ModelAdmin):
    search_fields = ["fecha"]

admin.site.register(dolar, DolarAdmin)

