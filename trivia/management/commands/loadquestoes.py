from django.core.management.base import BaseCommand, CommandError
from trivia.models import Pergunta, Resposta
import yaml

class Command(BaseCommand):
    args = '<filename>'
    help = 'Cria perguntas e respostas a partir de um arquivo yml'

    def handle(self, *args, **options):
        if not args:
            raise CommandError('informe o nome do arquivo yml')

        with open(args[0], 'r') as fs:
            perguntas = yaml.load(fs)
            for pergunta in perguntas:
                db_pergunta = Pergunta.objects.create(texto = pergunta.keys()[0])
                for i, resposta in enumerate(pergunta.values()[0]):
                    if i == 0:
                        correto = True
                    else:
                        correto = False
                    db_resposta = Resposta.objects.create(texto=unicode(resposta), pergunta=db_pergunta, correta=correto)

            self.stdout.write('%d perguntas carregadas com sucesso' % len(perguntas))
