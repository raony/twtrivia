from django.shortcuts import render, redirect
from random import randint, shuffle
from trivia.models import Pergunta, Resposta

# Create your views here.
def home(request):
    return render(request, 'trivia/home.html')

class Perguntas(object):
    def __init__(self, request):
        object.__setattr__(self, 'session', request.session)

    def __getattr__(self, attr):
        if attr == 'perguntas':
            return Pergunta.objects.filter(pk__in=self.session[attr])
        return self.session[attr]

    def __setattr__(self, name, value):
        self.session[name] = value

    def preparar_perguntas(self):
        perguntas = list(Pergunta.objects.all())
        shuffle(perguntas)
        self.perguntas = [p.pk for p in perguntas[:3]]
    
    def esta_preparado(self):
        return 'estados' in self.session and self.estados[-1] == 0

    @property
    def atual(self):
        return self.perguntas[self.indice]

    def acertou(self):
        self.estados[self.indice] = 1
        self.indice += 1

    def errou(self):
        self.estados[self.indice] = -1
        self.indice += 1

    def preparar(self):
        self.preparar_perguntas()
        self.estados = [0,0,0]
        self.indice = 0

def perguntas(request):
    p = Perguntas(request)
    if request.method == 'GET':
        if Pergunta.objects.all().count():
            if not p.esta_preparado():
                p.preparar()
            return render(request, 'trivia/questao.html', {
                'pergunta': p.atual,
                'estados': p.estados,
            })
        else:
            return redirect('home')
    if request.method == 'POST':
        resposta = Resposta.objects.get(texto=request.POST['resposta'], pergunta=p.atual)
        if resposta.correta:
            p.acertou()
        else:
            p.errou()
        return redirect('perguntas')

def reset(request):
    request.session.clear()
    return redirect('home')
