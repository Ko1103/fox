from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

def index(request):
    # template = loader.get_template('map/index.html')
    # return HttpResponse(template)
    return Http404('This page is not exist sorry')