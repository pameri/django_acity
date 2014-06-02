# Create your views here.
# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
#from portal.apps.osac.models import Ticket,TicketForm
#from portal.apps.home.forms import ContactForm, LoginForm
#from django.core.mail import EmailMultiAlternatives # Enviamos HTML
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout #,login,authenticate, get_user
from django.http import HttpResponseRedirect #, request
#from django.contrib.auth.models import User


#from django.contrib.auth import get_user    

#from django.http import HttpResponse
# Paginacion en Django
#from django.core.paginator import Paginator,EmptyPage,InvalidPage
#from django.shortcuts import render


def index_view(request):
    return render_to_response('home/index.html',context_instance=RequestContext(request))
 
#@login_required
#def index_ticket_view(request):     
#    return render_to_response('home/portada_ticket.html',context_instance=RequestContext(request))


def username(self):
    return self.user.name()

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

