
from django.contrib import admin
from .models import Cliente


# Register your models here.
@admin.register(Cliente)
class ClientesAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'cliente',
        'tipo',
        'telefone',
        'email',
        'endereco',
    )
    search_fields = ('cliente',)
    list_filter = ('tipo',)
