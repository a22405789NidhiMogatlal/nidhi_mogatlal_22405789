from django.contrib import admin
from .models import GeneroMusical, Banda, Festival
# Register your models here.

class GeneroMusicalAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class BandaAdmin(admin.ModelAdmin):
    list_display = ("nome", "genero")  
    ordering = ("nome",)
    search_fields = ("nome",)


class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


admin.site.register(GeneroMusical, GeneroMusicalAdmin)
admin.site.register(Banda, BandaAdmin)
admin.site.register(Festival, FestivalAdmin)
