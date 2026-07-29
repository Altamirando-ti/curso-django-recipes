from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse('Página home')

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return HttpResponse('Página sobre')

def contato(request):
    return HttpResponse('Página contato')