from django.contrib import admin
from artwark.models import ArtWark, Imagem, Participante

# Register your models here.

class ImagemInline(admin.TabularInline):
    model = Imagem

class ArtWarkAdmin(admin.ModelAdmin):
    inlines = [
        ImagemInline,
    ]

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'empresa', 'imagens']

admin.site.register(ArtWark, ArtWarkAdmin)
admin.site.register(Participante, ParticipanteAdmin)
