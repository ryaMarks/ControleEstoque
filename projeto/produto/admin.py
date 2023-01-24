from django.contrib import admin
from .models import Produto


# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'importado',
        'ncm',
        'preco',
        'estoque',
    )
    search_fields = ('produto',)
    list_filter = ('importado',)


