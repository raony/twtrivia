from django.contrib import admin
from trivia.models import Pergunta, Resposta

# Register your models here.
class RespostaInline(admin.TabularInline):
    model = Resposta

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [
        RespostaInline,
    ]

admin.site.register(Pergunta, PerguntaAdmin)
