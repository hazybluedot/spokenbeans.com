from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date, timedelta
from SnB.coffee.models import Origin
# Create your views here.

def origins(request):
    origin_list = Origin.objects.filter(blend=False)
    c = {'origin_list': origin_list}
    return render_to_response('origins.html', c)
 
