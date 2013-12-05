from django.shortcuts import render, redirect
from random import randint
from artwark.models import ArtWark, Imagem, Participante
from artwark.forms import ParticipanteForm

# Create your views here.
def home(request):
    if 'imagens' in request.session:
        if len(request.session['imagens']) >= 3:
            return redirect('artwark_maximo')
        img = Imagem.objects.get(pk=request.session['imagens'][-1])
    else:
        request.session['imagens'] = []
        artwark = ArtWark.objects.get(current=True)
        disponiveis = artwark.imagens.exclude(locked=True)
        if disponiveis.count():
            img = disponiveis[randint(0,disponiveis.count()-1)]
            img.locked = True
            img.save()
            request.session['imagens'].append(img.pk)
        else:
            return redirect('artwark_acabou')
    return render(request, 'artwark/home.html', {'img': img})

def reset(request):
    request.session.clear()
    return redirect('artwark_home')

def acabou(request):
    return render(request, 'artwark/acabou.html')

def maximo(request):
    return render(request, 'artwark/maximo.html')

def assinar(request):
    if request.method == 'GET':
        if 'participante' in request.session:
            form = ParticipanteForm(instance=Participante.objects.get(pk=request.session['participante']))
        else:
            form = ParticipanteForm()
    elif request.method == 'POST':
        try:
            form = ParticipanteForm(request.POST, instance=Participante.objects.get(email=request.POST['email']))
        except Participante.DoesNotExist:
            form = ParticipanteForm(request.POST)
        if form.is_valid():
            participante = form.save(commit=False)
            participante.imagens = len(request.session['imagens'])
            participante.save()
            request.session['participante'] = participante.pk
            return redirect('artwark_agradecimento')
    return render(request, 'artwark/assinar.html', {
        'form': form,
    })

    return render(request, 'artwark/assinar.html')

def agradecimento(request):
    return render(request, 'artwark/agradecimento.html')

def proxima(request):
    if 'imagens' not in request.session:
        return redirect('home')
    if len(request.session['imagens']) == 3:
        return redirect('artwark_maximo')
    artwark = ArtWark.objects.get(current=True)
    disponiveis = artwark.imagens.exclude(locked=True)
    if disponiveis.count():
        img = disponiveis[randint(0,disponiveis.count()-1)]
        img.locked = True
        img.save()
        request.session['imagens'].append(img.pk)
    else:
        redirect('artwark_acabou')
    request.session.modified = True
    return redirect('artwark_home')

