from rest_framework import serializers
from ..produto import models as modelsProduto
from ..clientes import models as modelsClientes

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = modelsProduto.Produto
        fields = '__all__'

class ClientsSerializers(serializers.ModelSerializer):
    class Meta:
        model = modelsClientes.Cliente
        fields = '__all__'


