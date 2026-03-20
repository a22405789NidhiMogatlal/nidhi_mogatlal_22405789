from django.contrib import admin
from .models import *


# Register your models here.
class GinasioAdmin(admin.ModelAdmin):
    list_display=("nome",)
    ordering=("nome",)
    search_fields=("nome",)

class PersonalTrainerAdmin(admin.ModelAdmin):
    list_display=("nome","ginasio",)
    ordering=("nome",)
    search_fields=("nome",)


class ClienteAdmin(admin.ModelAdmin):
    list_display=("nome","ginasio",)
    ordering=("nome",)
    search_fields=("nome",)

class SessaoAdmin(admin.ModelAdmin):
    list_display=("data","hora","pt","cliente")
    ordering=("data","hora",)
    search_fields=("cliente",)


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(PersonalTrainer,PersonalTrainerAdmin)
admin.site.register(Ginasio,GinasioAdmin)
admin.site.register(Sessao,SessaoAdmin)
