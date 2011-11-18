from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    HttpResponseRedirect("/static/index.html")
