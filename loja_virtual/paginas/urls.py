from django.urls import path

from .views import paginaInicioView, paginaAboutView, paginaProdutoView, paginaHomeView, paginaCadastroView, paginaContatoView, paginaLoginView
from .views import OrcamentoListView, OrcamentoDetailView
urlpatterns =[
    path('', paginaInicioView, name='inicio'),
    path('sobre/', paginaAboutView, name='sobre'),
    path('produto/',paginaProdutoView, name='produto'),
    path('home/', paginaHomeView, name='home'),
    path('cadastro/', paginaCadastroView, name='cadastro'),
    path('contato/', paginaContatoView, name='contato'),
    path('login/', paginaLoginView, name='login'),
    path('orcamentos/', OrcamentoListView.as_view(), name='orcamentos'),
    path('orcamentos/<int:pk>/', OrcamentoDetailView.as_view(), name='orcamento_detail')
]