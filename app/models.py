from django.db import models

# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "Cidades"
    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField(max_length=1000)
    cpf = models.CharField(max_length = 150)
    email = models.CharField(max_length = 1000)
    class Meta: 
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f'{self.nome} {self.cpf} {self.email}'
    
class Genero(models.Model):
    nome = models.CharField(max_length=100)
    class Meta: 
        verbose_name_plural = "Generos"
    def __str__(self):
        return self.nome
    

class Editora(models.Model):
    nome = models.CharField(max_length = 100)
    site = models.CharField(max_length = 100)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)
    class Meta:
        verbose_name_plural = 'Editoras'
    def __str__(self):
        return f'{self.nome} {self.site} {self.cidade}'
            
class Autor(models.Model):
    nome = models.CharField(max_length = 100)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)
    class Meta:
        verbose_name_plural = 'Autores'
    def __str__(self):
        return f'{self.nome} {self.cidade}'
    
class Livro(models.Model):
    nome = models.CharField(max_length = 100)
    genero = models.ForeignKey(Genero, on_delete = models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete = models.CASCADE)
    preco = models.DecimalField(max_digits = 10, decimal_places= 2)
    datapubli = models.DateField()
    class Meta:
        verbose_name_plural = 'Livros'
    def __str__(self):
        return f'{self.nome} {self.genero} {self.autor} {self.editora} {self.preco} {self.datapubli}'

class Emprestlivro(models.Model):
    dataemprest = models.DateField()
    livro = models.ForeignKey(Livro, on_delete = models.CASCADE)
    datadevo = models.DateField()
    leitor = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    class Meta:
        verbose_name_plural = 'Emprestlivro'
    def __str__(self):
        return f' {self.dataemprest} {self.livro} {self.datadevo} {self.leitor}'

    
