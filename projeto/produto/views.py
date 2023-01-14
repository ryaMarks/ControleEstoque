from django.shortcuts import render
from .models import Produto
# Create your views here.


def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(produto__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context)


def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    search = request.GET.get('search')
    if search:
        obj = obj.filter(produto__icontains=search)
    context = {'object': obj}
    return render(request, template_name, context)
