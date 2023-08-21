from rest_framework import viewsets
from ..api import serializers
from ..produto import models as modelsProduct
from ..clientes import models as modelsClients

class ProductsViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ProductsSerializers
    queryset = modelsProduct.Produto.objects.all()

class ClientsViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ClientsSerializers
    queryset = modelsClients.Cliente.objects.all()

