import string
from django.db import models

# Create your models here.
class ArtWark(models.Model):
    altura = models.IntegerField()
    largura = models.IntegerField()
    current = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        result = super(ArtWark, self).save(*args, **kwargs)
        if not self.imagens.all().count():
            for y in range(1,self.altura+1):
                for x in range(1,self.largura+1):
                    Imagem.objects.create(artwark=self, x=x, y=y)
        return result


class Imagem(models.Model):
    artwark = models.ForeignKey(ArtWark, related_name='imagens')
    arquivo = models.ImageField(null=True, upload_to=lambda instance, filename: 'artwark/%d/%d_%d.png'%(instance.artwark.pk, instance.x, instance.y))
    x = models.IntegerField()
    y = models.IntegerField()
    locked = models.BooleanField(default=False)

    @property
    def coluna(self):
        return list(string.ascii_uppercase)[self.x-1]

    @property
    def linha(self):
        return self.y

class Participante(models.Model):
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
    imagens = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nome_completo

    @property
    def nome_completo(self):
        return u'%s %s'%(self.nome, self.sobrenome)


