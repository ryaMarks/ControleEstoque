from django.shortcuts import render
from .models import Estoque, Estoque

# Create your views here.
def estoque_entrada_list(request):
    template_name = 'estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento='e')
    context = {'object_list': objects}
    return render(request, template_name, context=context)


def estoque_entrada_detail(request, pk):
    template_name = 'estoque_entrada_detail.html'
    obj = Estoque.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)
