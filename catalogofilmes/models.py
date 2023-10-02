from django.db import models
from django.utils import timezone


class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    url_da_capa = models.URLField(default='https://www.intercabos.com.br/wp-content/uploads/produto-sem-imagem.jpg')
    diretor = models.CharField(max_length=200, default='Não informado')
    faixa_etaria = models.IntegerField(default=0)
    data_lancamento = models.DateField(default=timezone.now)
    resumo = models.TextField()
    nota = models.FloatField(default=0)
    
    def __str__(self):
        return self.titulo