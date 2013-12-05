from django.contrib import admin
from artwark.models import ArtWark, Imagem

# Register your models here.

class ImagemInline(admin.TabularInline):
    model = Imagem

class ArtWarkAdmin(admin.ModelAdmin):
    inlines = [
        ImagemInline,
    ]

admin.site.register(ArtWark, ArtWarkAdmin)
