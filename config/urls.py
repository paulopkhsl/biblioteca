from django.contrib import admin
from django.urls import path
from app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('livros/', LivroView.as_view(), name='livros'),
    path('reserva/', EmprestlivroView.as_view(), name='reserva'),
    path('cidade/', CidadeView.as_view(),name='cidade'),
    path('autor/', AutorView.as_view(), name='autor'),
    path('editor/', EditoraView.as_view(),name='editora'),
    path('leitor/', UsuarioView.as_view(),name='usario'),
    path('genero/', GeneroView.as_view(),name='genero'),
    path('admin/', admin.site.urls),
]