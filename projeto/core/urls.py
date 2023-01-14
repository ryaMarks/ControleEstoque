from django.urls import path

from ..core import views as v

app_name = 'projeto.core'


urlpatterns = [
    path('', v.index, name='index'),
]
