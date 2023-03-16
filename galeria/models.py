from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False) #Campo char, maximo de 100 caracteres e não aceita null ou vazio
    legenda = models.CharField(max_length=150, null=False, blank=False) 
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self): #altera o retorno da string do objeto, junto de um print ou str(), ao inves de trazer a localização na memoria, traz uma string personalizada
        return f"Fotografia [nome={self.nome}]"
# Create your models here.


#migration é uma definição de uma tabela de dados