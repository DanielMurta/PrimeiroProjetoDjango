from django.shortcuts import render
from django.http import HttpResponse

def ver_cliente(requeste):
    return render(requeste, 'ver_cliente.html', {'nome': 'Daniel'})
