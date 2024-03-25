from django.shortcuts import render
from .models import *
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'index.html')
    def post(self, request):
        pass
    
class LivroView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'livros.html', {'livros':livros})
# def post(self, request, *args, **kwargs):
    
class EmprestlivroView(View):
    def get(self, request, *args, **kwargs):
        reservas = Emprestlivro.objects.all()
        return render(request, 'reserva.html',{'reservas': reservas})
    
class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades':cidades})
    
class AutorView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores':autores})
    
class EditoraView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html',{'editoras': editoras})
    
class UsuarioView(View):
    def get(self, request, *args, **kwargs):
        leitores = Usuario.objects.all()
        return render(request, 'leitor.html',{'leitores': leitores})
    
class GeneroView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos':generos})
    
