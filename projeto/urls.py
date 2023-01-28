

from django.contrib.auth.views import logout_then_login
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
# carregando arquivos estaticos no deploy: https://tutorial.djangogirls.org/pt/deploy/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projeto.core.urls')),
    path('clientes/', include('projeto.clientes.urls')),
    path('produto/', include('projeto.produto.urls')),
    path('estoque/', include('projeto.estoque.urls')),
    path('logout/', logout_then_login, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
