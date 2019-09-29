from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Orcamento
# Create your views here.

def paginaInicioView(req):
    if req.method == 'GET':
        print(req.headers)
        return HttpResponse('<h1>AC02 Completa!</h1>')

def paginaAboutView(req):
    return render(req, 'paginas/about.html', {})

def paginaProdutoView(req):
    return HttpResponse('<h2>Esta seria uma pagina com informação de um produto!</h2>')

def paginaHomeView(req):
    return render(req, 'paginas/home.html', {})

def paginaCadastroView(req):
    return render(req, 'paginas/cadastro.html', {})

def paginaLoginView(req):
    return render(req, 'paginas/login.html', {})

def paginaContatoView(req):
    return render(req, 'paginas/contato.html', {})


class OrcamentoListView(ListView):
    model = Orcamento
    template_name = "paginas/orcamentos.html"

class OrcamentoDetailView(DetailView):
    model = Orcamento
    template_name = "paginas/orcamento_detail.html"