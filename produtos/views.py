from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Resposável pela lógica da aplicação
# Cliente faz um requeste(Pedido) e o Servidor devolve uma response

def ver_produto(request):  # Requisição do usuário
    return render(request, 'ver_produto.html')

def inserir_produto(requeste):
    return HttpResponse('Inserindo Produtos')