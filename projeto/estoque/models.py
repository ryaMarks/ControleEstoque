from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from ..core.models import TimeStampedModel
from ..produto.models import Produto
# Create your models here.

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)


class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%Y'))

    def get_absolute_url(self):
        return reverse_lazy('estoque:estoque_entrada_detail', kwargs={'pk': self.pk})

    def nf_formated(self):
        return str(self.nf).zfill(3)


class EstoqueEntradaManager(models.Manager):
    def get_queryset(self):
        return super(EstoqueEntradaManager, self).get_queryset().filter(movimento='e')


class EstoqueEntrada(Estoque):
    objects = EstoqueEntradaManager()
    class Meta:
        proxy = True
        verbose_name = 'estoque_entrada'
        verbose_name_plural = 'estoque_entrada'


class EstoqueSaidaManager(models.Manager):
    def get_queryset(self):
        return super(EstoqueSaidaManager, self).get_queryset().filter(movimento='s')


class EstoqueSaida(Estoque):
    objects = EstoqueSaidaManager()
    class Meta:
        proxy = True
        verbose_name = 'estoque_saida'
        verbose_name_plural = 'estoque_saida'


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='estoques'
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)
