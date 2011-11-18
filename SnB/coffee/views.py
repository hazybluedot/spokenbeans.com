from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date, timedelta
from SnB.coffee.models import Origin
# Create your views here.

def origins():
    origin_list = Origin.objects.all()
    c = {'origin_list': origin_list}
    return render_to_response('orgins.html', c)
 
