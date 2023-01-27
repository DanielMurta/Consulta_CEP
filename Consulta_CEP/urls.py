from django.contrib import admin
from django.urls import path
from consulta import views


# Definindo Rotas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home')
]
