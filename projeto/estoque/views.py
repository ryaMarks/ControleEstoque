from django.contrib.auth.decorators import login_required
from django.shortcuts import render, resolve_url
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from ..produto.models import Produto
from .forms import EstoqueForm, EstoqueItensForm
from .models import Estoque, EstoqueEntrada, EstoqueSaida, EstoqueItens
# Create your views here.


class EstoqueEntradaList(ListView):
    model = EstoqueEntrada
    template_name = 'estoque_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(EstoqueEntradaList, self).get_context_data(**kwargs)
        context['titulo'] = 'Entrada'
        context['url_add'] = 'estoque:estoque_entrada_add'
        return context


class EstoqueDetail(DetailView):
    model = Estoque
    template_name = 'estoque_detail.html'


@login_required
def dar_baixa_estoque(form):
    # pega os produtos a partir de (estoque)
    produtos = form.estoques.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        produto.estoque = item.saldo
        produto.save()

@login_required
def estoque_add(request, template_name, movimento, url):
    estoque_form = Estoque()
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,
        can_delete=False,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(request.POST, instance=estoque_form, prefix='estoque')
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.movimento = movimento
            form.funcionario = request.user
            form.save()
            formset.save()
            dar_baixa_estoque(form)
            return {'pk': form.pk}
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')
    context = {'form': form, 'formset': formset}
    return context


@login_required
def estoque_entrada_add(request):
    template_name = 'estoque_entrada_form.html'
    movimento = 'e'
    url = 'estoque:estoque_detail'
    context = estoque_add(request, template_name, movimento, url)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


class EstoqueSaidaList(ListView):
    model = EstoqueSaida
    template_name = 'estoque_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(EstoqueSaidaList, self).get_context_data(**kwargs)
        context['titulo'] = 'Saida'
        context['url_add'] = 'estoque:estoque_saida_add'
        return context


class EstoqueSaidaDetail(DetailView):
    model = EstoqueSaida
    template_name = 'estoque_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EstoqueSaidaDetail, self).get_context_data(**kwargs)
        context['url_list'] = 'estoque:estoque_saida_list'
        return context


@login_required
def estoque_saida_add(request):
    template_name = 'estoque_saida_form.html'
    movimento = 's'
    url = 'estoque:estoque_detail'
    context = estoque_add(request, template_name, movimento, url)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)

