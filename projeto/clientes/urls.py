from django.urls import path
from ..clientes import views as v

app_name = 'clientes'
urlpatterns = [
    path('', v.ClientesList.as_view(), name='clientes_list'),
    path('add/', v.add_client.as_view(), name='clientes_add'),
    path('<int:pk>/', v.cliente_detail, name='cliente_detail'),
    path('<int:pk>/edit/', v.ClienteUpdate.as_view(), name='cliente_edit'),
    path('delete/<int:pk>', v.cliente_delete, name='cliente_delete'),
]
