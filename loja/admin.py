from django.contrib import admin
from .models import Loja,Categoria, Produto, Cliente, Pedido, Item
# Register your models here.


class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ("nome",)
    search_fields = ('nome',)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria')
    ordering = ('nome',)
    search_fields = ('nome',)
    


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'morada')
    ordering = ('nome',)
    search_fields = ('nome', 'morada')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto','quantidade',)
    ordering = ('quantidade',)
    search_fields = ('produto__nome',)
    


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data_criacao')
    ordering = ('data_criacao',)
    search_fields = ('cliente__nome',)
  


admin.site.register(Loja, LojaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Pedido, PedidoAdmin)