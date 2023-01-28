from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm
from django.views.generic import CreateView, ListView


# Create your views here.
class add_client(CreateView):
    model = Cliente
    template_name = 'clientes_add.html'
    form_class = ClienteForm


class ClientesList(ListView):
    model = Cliente
    template_name = 'clientes_list.html'
    paginate_by = 10


@login_required
def cliente_delete(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return render(request, 'clientes_list.html')


@login_required
def cliente_detail(request, pk):
    template_name = 'cliente_detail.html'
    obj = Cliente.objects.get(pk=pk)
    search = request.GET.get('search')
    if search:
        obj = obj.filter(cliente__icontains=search)
    context = {'object': obj}
    return render(request, template_name, context)
