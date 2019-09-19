from django.urls import path

from .views import paginaInicioView, paginaAboutView, paginaProdutoView, paginaHomeView

urlpatterns =[
    path('', paginaInicioView, name='inicio'),
    path('sobre/', paginaAboutView, name='sobre'),
    path('produto/',paginaProdutoView, name='produto'),
    path('home/', paginaHomeView, name='home')
]