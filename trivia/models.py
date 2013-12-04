from django.db import models
import math
import random

# Create your models here.

class Pergunta(models.Model):
    texto = models.CharField(max_length=255)

    def __unicode__(self):
        return self.texto

    def respostas_random(self):
        result = list(self.respostas.all())
        random.shuffle(result)
        print result
        return result

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, related_name="respostas")
    texto = models.CharField(max_length=255)
    correta = models.BooleanField(default=False)

    def __unicode__(self):
        return self.texto

class Jogador(models.Model):
    PAPEIS = (
        (0, 'CIO/CTO'),
        (1, 'Consultor'),
        (2, 'Gerente'),
        (3, 'Diretor'),
        (4, 'VP'),
        (5, 'Outro'),
    )
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    papel = models.IntegerField(choices=PAPEIS)
    melhor_tempo = models.IntegerField()

    def __unicode__(self):
        return self.nome_completo

    @property
    def nome_completo(self):
        return u'%s %s'%(self.nome, self.sobrenome)

    def tempo_formatado(self):
        minutos = math.floor(math.floor(self.melhor_tempo/1000)/60)
        segundos = math.floor(self.melhor_tempo/1000) - minutos*60
        miliseg = self.melhor_tempo - segundos*1000 - minutos*60000

        return '%d:%02d:%03d'%(minutos, segundos, miliseg)

