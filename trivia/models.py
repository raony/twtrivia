from django.db import models
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
