from django.contrib import admin
from trivia.models import Pergunta, Resposta, Jogador

# Register your models here.
class RespostaInline(admin.TabularInline):
    model = Resposta

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [
        RespostaInline,
    ]

class JogadorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'empresa', 'melhor_tempo', 'tempo_formatado']

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Jogador, JogadorAdmin)
