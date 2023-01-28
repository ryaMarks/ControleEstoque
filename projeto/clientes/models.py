from django.db import models
from django.urls import reverse_lazy


# variaveis de lista
PESSOA_TIPO = (
    ('---', '---'),
    ('Pessoa Física', 'Pessoa Física'),
    ('Pessoa Juridica', 'Pessoa Jurídica'),
)


# Create your models here.
class Cliente(models.Model):
    tipo = models.CharField(max_length=50, choices=PESSOA_TIPO, default='---')
    cliente = models.CharField('Nome', max_length=50, unique=True)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.CharField('E-Mail', max_length=50)
    endereco = models.CharField('Endereço completo', max_length=150)

    class Meta:
        ordering = ('cliente', )

    def __str__(self):
        return self.cliente

    def get_absolute_url(self):
        return reverse_lazy('clientes:cliente_detail', kwargs={'pk': self.pk})
