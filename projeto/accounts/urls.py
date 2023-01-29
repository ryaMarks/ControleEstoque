from django.urls import path
from ..accounts import views as v

app_name = 'accounts'
urlpatterns = [
    path('login/', v.user_login, name='login'),
]
