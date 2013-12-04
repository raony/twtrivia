import math
from django.shortcuts import render, redirect
from random import randint, shuffle
from trivia.models import Pergunta, Resposta, Jogador
from trivia.forms import JogadorForm
from datetime import datetime
from dateutil import parser

# Create your views here.
def home(request):
    return render(request, 'trivia/home.html')

class Perguntas(object):

    ACERTO = 1
    ERRO = -1
    VAZIO = 0

    def __init__(self, request):
        object.__setattr__(self, 'session', request.session)
        object.__setattr__(self, 'n_perguntas', 3)

    def __getattr__(self, attr):
        if attr == 'perguntas':
            return Pergunta.objects.filter(pk__in=self.session[attr])
        elif attr == 'tempo_inicial':
            return parser.parse(self.session[attr])
        elif attr == 'tempo_final':
            minutos = math.floor(math.floor(self.session[attr]/1000)/60)
            segundos = math.floor(self.session[attr]/1000) - minutos*60
            miliseg = self.session[attr] - segundos*1000 - minutos*60000

            return '%d:%02d:%03d'%(minutos, segundos, miliseg)
        elif attr == 'jogador':
            return Jogador.objects.get(pk=self.session[attr])
        return self.session[attr]

    def __setattr__(self, name, value):
        self.session[name] = value

    def preparar_perguntas(self):
        perguntas = list(Pergunta.objects.all())
        shuffle(perguntas)
        self.perguntas = [p.pk for p in perguntas[:self.n_perguntas]]
    
    def esta_preparado(self):
        return 'estados' in self.session and self.estados[-1] == 0

    @property
    def atual(self):
        return self.perguntas[self.indice]

    def acertou(self):
        self.estados[self.indice] = Perguntas.ACERTO
        self.indice += 1
        if self.acabou():
            self.tempo_final = self.tempo_atual

    def errou(self):
        self.estados[self.indice] = Perguntas.ERRO
        self.indice += 1

    def preparar(self):
        self.preparar_perguntas()
        self.estados = [Perguntas.VAZIO for i in range(self.n_perguntas)]
        self.indice = 0
        self.tempo_inicial = datetime.today().time().isoformat()

    def finalizou_com_sucesso(self):
        return all((estado == Perguntas.ACERTO for estado in self.estados))

    def acabou(self):
        return self.indice >= self.n_perguntas

    @property
    def tempo_atual(self):
        return math.floor((datetime.today() - self.tempo_inicial).total_seconds()*1000)

    @property
    def sucessos(self):
        return len([x for x in self.estados if x == Perguntas.ACERTO])

    @property
    def tem_jogador(self):
        return 'jogador' in self.session

    @property
    def tempo_final_raw(self):
        return self.session['tempo_final']


def perguntas(request):
    p = Perguntas(request)
    if request.method == 'GET':
        if Pergunta.objects.all().count():
            if not p.esta_preparado():
                p.preparar()
            return render(request, 'trivia/questao.html', {
                'pergunta': p.atual,
                'estados': p.estados,
                'tempo': p.tempo_atual,
            })
        else:
            return redirect('home')
    if request.method == 'POST':
        resposta = Resposta.objects.get(texto=request.POST['resposta'], pergunta=p.atual)
        if resposta.correta:
            p.acertou()
        else:
            p.errou()

        if p.acabou():
            if p.finalizou_com_sucesso():
                return redirect('sucesso')
            else:
                return redirect('falhou')
        return redirect('perguntas')

def reset(request):
    request.session.clear()
    return redirect('home')

def sucesso(request):
    p = Perguntas(request)
    if not p.acabou():
        return redirect('perguntas')
    if request.method == 'GET':
        if p.tem_jogador:
            form = JogadorForm(instance=p.jogador)
        else:
            form = JogadorForm()
    elif request.method == 'POST':
        try:
            form = JogadorForm(request.POST, instance=Jogador.objects.get(email=request.POST['email']))
        except Jogador.DoesNotExist:
            form = JogadorForm(request.POST)
        if form.is_valid():
            jogador = form.save(commit=False)
            if not jogador.melhor_tempo or p.tempo_final_raw < jogador.melhor_tempo:
                jogador.melhor_tempo = p.tempo_final_raw
            jogador.save()
            p.jogador = jogador.pk
            return redirect('ranking')
    return render(request, 'trivia/sucesso.html', {
        'tempo': p.tempo_final,
        'form': form,
    })


def falhou(request):
    p = Perguntas(request)
    if not p.acabou():
        return redirect('perguntas')
    return render(request, 'trivia/falhou.html', {
        'acertos': p.sucessos,
        'total': p.n_perguntas,
    })
