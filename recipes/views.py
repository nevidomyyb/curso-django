from django.http import HttpResponse
from django.shortcuts import render


def home(Request):
    return HttpResponse("HOME 1")

def sobre(Request):
    return HttpResponse("SOBRE 1")

def contato(Request):
    return HttpResponse("CONTATO 1")
# Create your views here.
