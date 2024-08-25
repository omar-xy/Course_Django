
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader 

def handler404(request, exception):
    return HttpResponseNotFound('<h1> Page Not Found </h1>')
